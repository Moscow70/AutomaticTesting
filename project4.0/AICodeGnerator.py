from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path
import ast
import re
from typing import Dict, Union, List

load_dotenv(dotenv_path="../.env", override=True)

OPENAI_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
OPENAI_BASE_URL = os.environ.get("DEEPSEEK_BASE_URL")

class AICodeGenerator:
    """支持全局约束感知的代码注释工具"""
    
    def __init__(self, 
                 constraints: Dict[str, Dict[str, Union[str, int, List[str]]]],
                 chunk_size,
                 model: str = "deepseek-reasoner"):
        """
        :param constraints: 结构化约束字典 {字段名: {约束键: 约束值}}
        :param chunk_size: 单次处理代码块的最大长度（字符数）
        """
        self.client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)
        self.model = model
        self.constraints = constraints
        self.chunk_size = chunk_size
        self.context_buffer = []

    def annotate_file(self, input_path: str, output_path: str):
        """带约束传播的注释流程"""
        raw_code = Path(input_path).read_text(encoding='utf-8')
        chunks = self._chunk_code(raw_code)
        
        annotated_chunks = []
        for chunk in chunks:
            # print(chunk)
            prompt = self._build_prompt(chunk)
            response = self._get_llm_response(prompt)
            annotated = self._integrate_context(chunk, response)
            annotated_chunks.append(annotated)
            
        Path(output_path).write_text('\n'.join(annotated_chunks), encoding='utf-8')

    def _chunk_code(self, code: str) -> List[str]:
        """改进版智能分块"""
        tree = ast.parse(code)
        chunks = []
        current_chunk = []
        current_length = 0
        padding_lines = 3  # 上下文保留行数
        
        for node in ast.iter_child_nodes(tree):
            node_code = ast.get_source_segment(code, node)
            if not node_code:
                continue                
            node_length = len(node_code)
            
            # 遇到类/方法定义时提交当前块
            if isinstance(node, (ast.ClassDef, ast.FunctionDef)):
                if current_chunk:
                    chunks.append('\n'.join(current_chunk))
                    current_chunk = []
                    current_length = 0
                
                current_chunk.extend(node_code.split('\n'))
                current_length += node_length
            else:
                lines = node_code.split('\n')
                for line in lines:
                    if current_length + len(line) > self.chunk_size:
                        if len(current_chunk) > padding_lines*2:
                            # 保留最后3行作为上下文
                            chunks.append('\n'.join(current_chunk[:-padding_lines]))
                            current_chunk = current_chunk[-padding_lines:]
                            current_length = sum(len(l) for l in current_chunk)
                        else:
                            chunks.append('\n'.join(current_chunk))
                            current_chunk = []
                            current_length = 0
                    current_chunk.append(line)
                    current_length += len(line) + 1  # +1 for newline
        
        if current_chunk:
            chunks.append('\n'.join(current_chunk))
            
        return chunks

    def _build_prompt(self, code_chunk: str) -> str:
        """在全局约束条件下修改代码"""
        return f"""
        请根据用户输入的要求修改输入的代码并输出全新的代码，要求：
        1. 通过读取每行代码的注释（如果有）识别每个操作的业务目的（如：输入用户名、验证密码复杂度），如果多行代码属于同一操作，请阅读最前面的注释。
        2. 当发现用户输入的要求的部分的代码时，进行修改，其它时候保持原始代码不变。
        3. 当当前代码块中不包含需要修改的部分时，直接返回原始代码，不要添加新的代码和注释，不要解释为什么保持原始代码不变。
        3. 仅修改用户输入中要求的部分，其它部分保持原始代码不变，不要添加任何新的代码或注释。
        4. 关联相关约束条件（见下方）。
        
        
        当前代码块：
        {code_chunk}
        
        全局约束条件：
        {self._format_constraints()}
        
        历史上下文（最近3个操作）：
        {self._get_recent_context()}

        用户要求：
        {self._get_user_requirements()}
        
        注释示例格式：
        element.send_keys("test")  # 输入测试数据 [约束：用户账号]
        """

    def _format_constraints(self) -> str:
        """约束条件格式化（支持多类型值）"""
        formatted = []
        for field, rules in self.constraints.items():
            rule_strs = []
            for key, value in rules.items():
                if isinstance(value, list):
                    rule_strs.append(f"{key}: {', '.join(value)}")
                else:
                    rule_strs.append(f"{key}: {value}")
            formatted.append(f"{field}: {'; '.join(rule_strs)}")
        return '\n'.join(formatted)

    def _get_recent_context(self) -> str:
        """获取最近相关的上下文"""
        return '\n'.join(self.context_buffer[-3:]) if self.context_buffer else "无"

    def _get_llm_response(self, prompt: str) -> str:
        """调用LLM接口"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{
                "role": "system",
                "content": "你是一个测试代码修改专家，擅长读取用户需求并在代码中定位相关部分，最后修改代码"
            }, {
                "role": "user",
                "content": prompt
            }],
            temperature=0.1,
            max_tokens=1500
        )
        return response.choices[0].message.content

    def _integrate_context(self, original: str, annotated: str) -> str:
        """整合上下文信息"""
        # 提取关键操作更新上下文
        new_actions = re.findall(r"#\s*(.*?)\[", annotated)
        self.context_buffer.extend(new_actions)
        
        # 保持上下文缓冲区大小
        if len(self.context_buffer) > 10:
            self.context_buffer = self.context_buffer[-7:]
            
        return annotated
    
    def _get_user_requirements(self) -> str:
        """获取用户输入的要求"""
        return f"""
        1. 这是一个通过关键词查询用户的代码。
        2. 修改输入的关键词，变更为查找kcgly。
        3. 输出新的代码。
        """

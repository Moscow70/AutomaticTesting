from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import re
from typing import Dict, List, Optional

from LLMTextFilter import LLMTextFilter

load_dotenv(dotenv_path="../.env", override=True)

OPENAI_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
OPENAI_BASE_URL = os.environ.get("DEEPSEEK_BASE_URL")

class SmartTableExtractor:
    def __init__(self):
        """
        初始化智能表格解析器
        
        :param api_key: OpenAI API密钥
        """
        self.client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)
        self.required_fields = ["name", "type"]  # 必要字段

        # 标准字段映射提示模板
        self.header_prompt = """
        # 角色
        你是一位专业的数据架构师，负责将技术文档中的表格列名映射到标准字段。

        # 任务
        将以下表格列名映射到标准字段（name/type/length/rules）：
        原始表头：{headers}

        # 标准字段定义
        1. name: 字段名称（如"用户账号"）
        2. type: 数据类型（字符/数字/日期/枚举）
        3. length: 长度限制（如"8-18"）
        4. rules: 业务约束（如"必填，允许汉字"）

        # 输出要求
        - 返回严格的JSON格式
        - 忽略无法识别的列
        - 示例输入：["列名", "数据类别", "最大长度", "约束条件"]
        - 示例输出：{{"name": "列名", "type": "数据类别", "length": "最大长度", "rules": "约束条件"}}

        # 重要提示
        请直接返回JSON，不要包含任何解释性文字！
        """

    def extract_constraints(self, table_segment: List[List[List[str]]]) -> Dict[str, Dict]:
        """
        主方法：提取并返回结构化约束数据
        
        :param table_segment: 三维列表结构 [表格][行][列]
        """
        structured_data = {}

        for table in table_segment:
            if len(table) < 2:
                continue  # 跳过空表

            headers = table[0]
            try:
                # 步骤1：智能表头映射
                header_map = self._map_headers_with_llm(headers)
                header_indices = self._convert_names_to_indices(headers, header_map)                
                # 验证必要字段
                if not self._validate_header_mapping(header_indices):
                    continue

                # 步骤2：处理数据行
                for row in table[1:]:
                    constraint = self._process_row(row, header_indices)
                    if constraint["name"]:
                        structured_data[constraint["name"]] = constraint
            except Exception as e:
                print(f"处理表格时发生错误: {str(e)}")
                continue

        return structured_data

    def parse_json_response(self, response_text: str) -> Dict:
        """解析大模型返回的JSON字符串"""
        try:
            # 尝试直接解析
            return json.loads(response_text)
        except json.JSONDecodeError:
            # 预处理：提取JSON部分
            json_match = re.search(r"\{.*\}", response_text, re.DOTALL)
            if json_match:
                try:
                    return json.loads(json_match.group(0))
                except json.JSONDecodeError as e:
                    raise ValueError(f"提取的JSON无效: {str(e)}")
            raise ValueError("无法从响应中提取有效JSON")

    def _map_headers_with_llm(self, headers: List[str]) -> Dict[str, str]:
        """
        使用大模型映射表头到标准字段
        返回格式：{"标准字段": "原始列名"}
        """
        prompt = self.header_prompt.format(headers=json.dumps(headers, ensure_ascii=False))
        response = self.client.chat.completions.create(
            model="deepseek-reasoner",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=4096
        )
        print(response.choices[0].message.content)
        response_text = response.choices[0].message.content
        return self.parse_json_response(response_text)


    def _convert_names_to_indices(self, headers: List[str], header_map: Dict[str, str]) -> Dict[str, int]:
        """将列名映射转换为索引映射"""
        indices = {}
        for field, col_name in header_map.items():
            if col_name and col_name in headers:
                indices[field] = headers.index(col_name)
            else:
                indices[field] = -1  # 标记无效字段
        return indices

    def _validate_header_mapping(self, header_indices: Dict[str, int]) -> bool:
        """验证映射结果有效性"""
        # 检查必要字段是否有效
        for field in self.required_fields:
            if header_indices.get(field, -1) < 0:
                print(f"缺失或无效的必要字段: {field}")
                return False
        return True

    def _process_row(self, row: List[str], header_indices: Dict[str, int]) -> Dict:
        """使用整数索引处理数据行"""
        constraint = {
            "name": "",
            "type": "字符",
            "length": None,
            "raw_rules": "",
            "cleaned_rules": [],
            "allowed_values": [],
            "notes": ""
        }

        try:
            # 使用整数索引访问数据
            name_idx = header_indices.get("name", -1)
            if name_idx != -1 and name_idx < len(row):
                constraint["name"] = row[name_idx]

            type_idx = header_indices.get("type", -1)
            if type_idx != -1 and type_idx < len(row):
                constraint["type"] = row[type_idx]

            length_idx = header_indices.get("length", -1)
            if length_idx != -1 and length_idx < len(row):
                constraint["length"] = self._parse_length(row[length_idx])

            llm_filter = LLMTextFilter()

            rules_idx = header_indices.get("rules", -1)
            if rules_idx != -1 and rules_idx < len(row):
                raw_rules_str = row[rules_idx]
                constraint["raw_rules"] = self._parse_rules(raw_rules_str)

                cleaned_texts = llm_filter.filter_all_texts(raw_rules_str)

                constraint["cleaned_rules"] = self._parse_cleaned_rules(cleaned_texts)
                constraint["allowed_values"] = self._parse_allowed_values(cleaned_texts)

        except IndexError:
            pass  # 处理列数不足的情况

        return constraint

    def _parse_length(self, length_str: str) -> Optional[int]:
        """
        解析长度范围字符串，返回最大长度
        """
        if not length_str:
            return None
        
        # 处理不同格式：20、8-18、≤20
        length_str = length_str.strip()
        
        if "-" in length_str:  # 8-18 → 18
            return int(length_str.split("-")[-1])
        elif "≤" in length_str:  # ≤20 → 20
            return int(length_str.replace("≤", ""))
        elif length_str.isdigit():
            return int(length_str)
        
        return None

    def _parse_rules(self, rule_str: str) -> List[str]:
        """
        解析约束规则为结构化列表
        """
        if not rule_str:
            return []
        
        # 拆分规则：中文逗号/分号/句号分隔
        rules = re.split(r"[，；。、]", rule_str)
        return [rule.strip() for rule in rules if rule.strip()]
    
    def _parse_cleaned_rules(self, cleaned_text: str) -> List[str]:
        """解析清洗后的分点规则"""
        return [line.strip() for line in cleaned_text.split("\n") if line.strip()]

    def _parse_allowed_values(self, rule_str: str) -> List[str]:
        """
        从规则中解析允许的枚举值
        """
        if not rule_str:
            return []
        
        # 匹配模式：取值范围：值1、值2、值3
        pattern = r"取值(范围|选项)[：:]\s*([^。]+)"
        match = re.search(pattern, rule_str)
        if not match:
            return []
        
        values_str = match.group(2)
        # 支持中文/英文分隔符：、, / 
        return [v.strip() for v in re.split(r"[、,/\s]+", values_str) if v.strip()]

# # 使用示例
# if __name__ == "__main__":
#     # 示例输入数据（三维列表）
#     sample_tables = [
#         [
#             ["字段标识", "数据格式", "字符限制", "验证规则"],
#             ["username", "string", "5-20", "允许字母、数字、下划线"],
#             ["gender", "enum", "-", "取值范围：male, female"]
#         ],
#         [
#             ["参数名称", "类型", "长度", "约束"],
#             ["mobile", "string", "11", "必须符合手机号格式"]
#         ]
#     ]

#     extractor = SmartTableExtractor(api_key="your_openai_api_key")
    
#     try:
#         constraints = extractor.extract_constraints(sample_tables)
#         print("提取的约束信息：")
#         print(json.dumps(constraints, indent=2, ensure_ascii=False))
#     except Exception as e:
#         print(f"处理失败: {str(e)}")
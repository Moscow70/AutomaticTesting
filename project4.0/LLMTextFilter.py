from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv(dotenv_path="../.env", override=True)

OPENAI_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
OPENAI_BASE_URL = os.environ.get("DEEPSEEK_BASE_URL")

class LLMTextFilter:
    def __init__(self, model="deepseek-reasoner", max_retries=3):
        """
        初始化大模型文本筛查工具
        :param api_key: OpenAI API Key
        :param model: 模型名称，默认 gpt-4
        :param max_retries: API 调用失败最大重试次数
        """
        self.client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)
        self.model = model
        self.max_retries = max_retries

        # 定义提示词模板
        self.system_prompt = """
        # 角色
        你是一个专业的技术文档清洗机器人，负责从冗长的需求文档中提取核心技术需求，或提取变量约束。

        # 任务要求
        1. 保留所有的需求功能点或变量约束，删除无关内容。
        2. 保留所有需求功能点或变量约束的详细描述，删除无关内容。
        3. 删除项目进度、非技术性备注等无关内容。
        4. 删除页码、文档编号、标题、机构名称等无关内容。
        5. 删除无意义换行、空格、换行符等格式内容。
        6. 使用 Markdown 格式输出.
        7. 跳过表格内容，不做处理。
        8. 如果输入文本无意义，返回 "无有效内容"。
        9. 如果输入的文本非常简洁，意义明确，则直接返回输入文本。
        """

        self.user_prompt_template = """
        # 输入样例
        输入文本：
        \"\"\"
        用户管理只对系统管理员开放，实现用户的新增、编辑、详
        情、冻结、解冻、密 码重置、删除、查询。 
        用户信息包括：用户账号、用户姓名、头像、性别、手机号
        码、状态等，见表4.8.1 1。  
        （1）新增：实现用户新增的功能； 
        （2）编辑：实现用户信息的修改，用户账号不能进行修改； 
        （3）详情：查看用户的详细信息； 
        （4）冻结：实现用户的冻结功能，冻结后不得登录系统，状态
        变更为【冻结】； 
        （5）解冻：实现对状态为【冻结】用户的解冻功能，解冻后可
        以登录系统，状态 变更为【正常】； 
        （6）密码重置：实现用户密码的重置功能； 
        （7）删除：将用户从系统中删除，被楼号房号绑定的安全员和
        组长不能进行删除， 具有流程信息的其余用户不能进行删除； 
        （8）查询：根据用户账号、性别、用户姓名、手机号码和状态
        模糊查询符合条件 的用户。
        \"\"\"

        # 输出样例
        处理结果：
        \"\"\"
        用户管理模块功能需求：
        （1）新增：实现用户新增的功能； 
        （2）编辑：实现用户信息的修改，用户账号不能进行修改； 
        （3）详情：查看用户的详细信息； 
        （4）冻结：实现用户的冻结功能，冻结后不得登录系统，状态变更为【冻结】； 
        （5）解冻：实现对状态为【冻结】用户的解冻功能，解冻后可以登录系统，状态 变更为【正常】； 
        （6）密码重置：实现用户密码的重置功能； 
        （7）删除：将用户从系统中删除，被楼号房号绑定的安全员和组长不能进行删除， 具有流程信息的其余用户不能进行删除； 
        （8）查询：根据用户账号、性别、用户姓名、手机号码和状态模糊查询符合条件 的用户。
        \"\"\"

        # 当前任务
        输入文本：
        \"\"\"
        {input_text}
        \"\"\"
        """

    def _call_llm_api(self, user_prompt):
        """调用大模型 API（带重试机制）"""
        for _ in range(self.max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.3
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                print(f"API 调用失败: {e}, 5秒后重试...")
                time.sleep(5)
        return None

    def filter_text(self, text):
        """处理单个文本段落"""
        if not text.strip():
            return ""
            
        user_prompt = self.user_prompt_template.format(input_text=text)
        result = self._call_llm_api(user_prompt)
        
        # 处理异常情况
        if result is None:
            return "大模型处理失败"
        if "无有效内容" in result:
            return ""
        return result

    def filter_all_texts(self, text_list):
        """批量处理文本段落"""
        if isinstance(text_list, str):
            return self.filter_text(text_list)
        return [self.filter_text(text) for text in text_list]
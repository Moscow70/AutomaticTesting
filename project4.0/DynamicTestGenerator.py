import fitz
from selenium.webdriver.common.by import By
import re
import random
import string
from faker import Faker
from pathlib import Path

class DynamicTestGenerator:
    def __init__(self, pdf_path, code_path):
        self.pdf_path = pdf_path
        self.code_path = code_path
        self.constraints = {}
        self.field_operations = []
        self.fake = Faker(locale='zh_CN')
        self._parse_pdf()
        self._parse_code()

    def _parse_pdf(self):
        """从PDF提取字段约束"""
        doc = fitz.open(self.pdf_path)
        for page in doc:
            tables = page.find_tables()
            for table in tables:
                data = table.extract()
                if "名称" in data[0]:  # 假设第一行是表头
                    headers = data[0]
                    for row in data[1:]:
                        if len(row) >= 5:
                            field = row[1].strip()
                            self.constraints[field] = {
                                "类型": row[2].strip(),
                                "长度": int(row[3].split("-")[-1]),
                                "规则": row[4].strip()
                            }

    def _parse_code(self):
        """解析代码中的输入操作"""
        with open(self.code_path, "r", encoding="utf-8") as f:
            code = f.read()
        
        # 提取所有send_keys操作
        send_keys_matches = re.finditer(
            r'driver\.find_element(_by_xpath)?\(["\'](.*?)["\']\)\.send_keys\(["\'](.*?)["\']\)',
            code
        )
        
        # 分析上下文
        context = "登录"
        for match in send_keys_matches:
            xpath, value = match.group(2), match.group(3)
            if "用户管理" in code.split(match.group(0))[0]:
                context = "用户管理"
            
            self.field_operations.append({
                "xpath": xpath,
                "original_value": value,
                "context": context
            })

    def _map_field(self, operation):
        """映射操作到字段"""
        if "password" in operation["xpath"].lower():
            return "登录密码"
        elif operation["context"] == "用户管理":
            return "用户姓名"
        else:
            return "用户账号"

    def _generate_value(self, field):
        """根据约束生成测试数据"""
        constraint = self.constraints.get(field, {})
        
        if field == "用户账号":
            # 生成：汉字+小写字母+数字+特殊符号
            components = [
                self.fake.word()[:2], 
                ''.join(random.choices(string.ascii_lowercase, k=3)),
                ''.join(random.choices(string.digits, k=2)),
                random.choice(['_', '@', '#', '$'])
            ]
            return ''.join(components)[:constraint.get("长度", 20)]
        
        elif field == "登录密码":
            # 生成：大小写字母+数字+特殊符号
            components = [
                random.choice(string.ascii_uppercase),
                random.choice(string.ascii_lowercase),
                random.choice(string.digits),
                random.choice(['!', '@', '#', '$'])
            ] + random.choices(string.ascii_letters + string.digits, k=14)
            return ''.join(components)[:constraint.get("长度", 18)]
        
        elif field == "用户姓名":
            # 生成汉字姓名
            return self.fake.name()[:constraint.get("长度", 10)]
        
        return "default_value"

    def generate_test(self, output_path):
        """生成新的测试代码"""
        replacements = []
        for op in self.field_operations:
            field = self._map_field(op)
            new_value = self._generate_value(field)
            replacements.append((
                f'send_keys("{op["original_value"]}")',
                f'send_keys("{new_value}")  # {field}'
            ))

        # 替换原始代码
        with open(self.code_path, "r", encoding="utf-8") as f:
            code = f.read()
        
        for old, new in replacements:
            code = code.replace(old, new)
        
        # 更新过时的API调用
        code = code.replace("find_element_by_xpath", "find_element")
        code = re.sub(
            r'(driver\.find_element)\(["\'](.*?)["\']\)',
            r'\1(By.XPATH, "\2")',
            code
        )
        
        # 添加必要的import
        if "from selenium.webdriver.common.by import By" not in code:
            code = code.replace(
                "from selenium import webdriver",
                "from selenium import webdriver\nfrom selenium.webdriver.common.by import By"
            )
        
        # 保存生成的代码
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(code)
        return str(output_path)

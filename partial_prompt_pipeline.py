# 采用部分提示模板，引导用户获取精准服务。通过使用partial prompt template对不同阶段的提示语进行整合
# 或者通过将不同提示信息分成几个不同的模板，再将它们整合到一个大的模板里。通过pipelineprompttemplate来实现




import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts.pipeline import PipelinePromptTemplate
from langchain_community.llms.baidu_qianfan_endpoint import QianfanLLMEndpoint

load_dotenv(dotenv_path=".env", override= True)
QIANFAN_ACCESS_KEY = os.environ.get("QIANFAN_ACCESS_KEY")
QIANFAN_SECRET_KEY = os.environ.get("QIANFAN_SECRET_KEY")

llm = QianfanLLMEndpoint(model= "ERNIE-Lite-8K")

# def _get_os(brand):
#     os_dict = {
#         "iPhone" : "iOS",
#         "Samsung" : "Android",
#         "Huawei" : "HarmonyOS",
#         "Xiaomi" : "Android"
#     }
#     return os_dict.get(brand, "Unknown Operation System")

# prompt = PromptTemplate(template="我想知道如何在{brand}手机的{os}系统中进行出厂恢复操作？", input_variables=["brand", "os"])

# partial_prompt = prompt.partial(brand = "Huawei")

# formatted_prompt = str(partial_prompt.format(os = _get_os("Huawei")))

# response = llm.invoke(formatted_prompt)

# print(response)

# 使用pipelineprompttemplate集成多个模板

full_template = """
{category_select} {brand_select} {OS_select} {problem_select}
"""

full_prompt = PromptTemplate.from_template(full_template)

person_template = """您好，我是{person}，"""
person_prompt = PromptTemplate.from_template(person_template)
brand_template = """我了解到您使用的是{brand}手机，"""
brand_prompt = PromptTemplate.from_template(brand_template)
os_template = """操作系统为{os}。"""
os_prompt = PromptTemplate.from_template(os_template)
problem_template = """您遇到了{problem}问题，我可以为您解决"""
problem_prompt = PromptTemplate.from_template(problem_template)

# 组合模板的部分
input_prompts = [
    ("category_select", person_prompt),
    ("brand_select", brand_prompt),
    ("OS_select", os_prompt),
    ("problem_select", problem_prompt)
]

pipeline_prompt = PipelinePromptTemplate(final_prompt= full_prompt, pipeline_prompts= input_prompts)

formatted_prompt = pipeline_prompt.format(
    person = "技术支持",
    brand = "华为",
    os = "HarmonyOS",
    problem = "恢复出厂设置"
)
response = llm.invoke(formatted_prompt)
print(response)
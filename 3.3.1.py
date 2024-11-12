# 除了提示词模板之外，另一种不改变模型羁绊结构和参数的前提下能够唤醒模型能力并提高模型响应正确率的方法叫示例选择器。它们都被称为提示调优"prompt tuning"
# 客服交互设计：通过LengthBasedExampleSelector实现三步响应法。也即第一句直接回答用户问题，第二句对问题进行进一步的解释，第三句跟进询问用户


import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.baidu_qianfan_endpoint import QianfanLLMEndpoint
from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core .prompts import FewShotPromptTemplate

load_dotenv(dotenv_path=".env", override= True)
QIANFAN_ACCESS_KEY = os.environ.get("QIANFAN_ACCESS_KEY")
QIANFAN_SECRET_KEY = os.environ.get("QIANFAN_SECRET_KEY")

llm = QianfanLLMEndpoint(model= "ERNIE-Lite-8K")

examples = [
    {"input": "如何重置密码？", "output": "请前往登录页面，点击“忘记密码”链接，然后按照提示操作。这样您可以收到一个重置密码的链接，通过链接设置新的密码。是否解决了您的问题？"},
    {"input": "怎样查询订单状态？", "output": "请登录您的账户，然后点击“我的订单”查看订单状态。在“我的订单”页面，您可以看到订单的当前状态，例如“处理中”“已发货”或“已完成”。这对您有帮助吗？"},
    {"input": "如何申请退货？", "output": "请登录您的账户，找到相应的订单，点击申请退货按钮。系统将引导您完成退货申请流程，包括提供退货理由和退货地址。需要我为您提供其他帮助吗？"},
    {"input": "如何使用优惠券？", "output": "在结账页面，找到“使用优惠券”选项，输入优惠券代码。优惠券将会立即生效，您可以看到总价已经调整。还有其他我可以为您做的吗？"},
]

example_prompt = PromptTemplate(
    input_variables= ["input", "output"],
    template= "问题：{input}\n回答：{output}",
)

# 创建示例选择器
example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
)

# 创建动态提示模板，该对象定义了如何根据用户的查询生成提示。它包含了前缀、后缀和输入变量，以及一个示例选择器和一个示例提示模板。
dynamic_prompt = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt = example_prompt,
    # 指定将被添加到生成提示的开始部分的文本。为模型设置了一个场景，告诉模型将要执行什么样的任务
    prefix = "回答以下客户的问题，并提供额外的解释或信息，然后询问他们是否满意",
    # 指定将被添加到生成提示末尾部分的文本。通常用于提供更多的格式指示或进一步的指令
    suffix = "问题：{query}\n回答：",
    input_variables = ["query"],
)

# 格式化动态提示。通过打印结果可以看出格式化之后的提示信息
print(dynamic_prompt.format(query="如何取消订单？"))

output = llm.generate([dynamic_prompt.format(query="如何取消订单？")])
print(output)
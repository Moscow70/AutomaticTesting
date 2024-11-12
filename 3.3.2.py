# 用户请求归类：通过SemanticSimilarityExampleSelector实现相似度选择
# 当用户提问本身比较模糊，没有固定套路时，需要通过大模型将用户提示的问题进行分类。
# 由此，我们需要将用户输入与示例选择器内的示例相似度进行比较，将问题归类到问题分类当中。

# 这是语义相似度匹配器
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
# 这是向量数据库
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import QianfanEmbeddingsEndpoint
from langchain_community.llms.baidu_qianfan_endpoint import QianfanLLMEndpoint

llm = QianfanLLMEndpoint(model= "ERNIE-Lite-8K")

example_prompt = PromptTemplate(input_variables=["input", "output"], template= "示例输入：{input}\n示例输出：{output}")

examples = [
    {"input":"我忘记了密码，怎么重置？", "output":"账户问题"},
    {"input":"我的订单在哪里，已经过了一周了？", "output":"订单问题"},
    {"input":"我收到了一个有缺陷的物品，我怎么退货？", "output":"退货退款问题"},
    {"input":"我想更改我的送货地址。", "output":"订单问题"},
    {"input":"我怎么升级我的会员资格？", "output":"账户问题"},
    {"input":"我的订单被收了两次费，我该怎么办？", "output":"订单问题"},
    {"input":"送货的商品不是我订购的，我怎么换货？", "output":"退货退款问题"},
    {"input":"我怎么取消我的订单？", "output":"订单问题"},
    {"input":"我的优惠码不起作用，你能帮帮我吗？", "output":"促销问题"},
    {"input":"我无法登录我的账户，应该怎么办？", "output":"账户问题"}
]

# 创建语义相似性示例选择器
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    QianfanEmbeddingsEndpoint(),
    FAISS,
    k = 2
)

similar_prompt = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt = example_prompt,
    prefix = "以下是一个客户服务查询，请将其分类：",
    suffix = "输入：{query}\n输出：",
    input_variables=["query"],
)

my_query = "我的订单什么时候能到达？"

print(similar_prompt.format(query = my_query))
print("---------------------------------")
response = llm.generate([str(similar_prompt.format(query = my_query))])
print(response)

# 效果不好，没有按照给出的example分类
from openai import OpenAI
import json
import httpx
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env", override=True)

api_key = os.environ.get("OPENAI_API_KEY")
base_url = os.environ.get("OPENAI_API_BASE")


client = OpenAI(
    api_key = api_key,
    base_url = base_url
)

MODEL = "ERNIE-Lite-8K"

dataset = open('dataset.csv', 'r', encoding='utf-8').readlines()[1:]
reviews = []
labels = []
# 将评价和标签按照,分隔开来分别存储
for row in dataset:
    items = row.split(',')
    reviews.append(items[0])
    labels.append(items[1])

# embedding 是文本之间的向量相关性

# 实现文本转embedding的方法
def get_embedding(text, model = MODEL):
    return client.embeddings.create(input = [text], model = model).data[0].embedding

# 设立标准，将文本变为向量
positive = get_embedding("好评")
negative = get_embedding("差评")

# 将review变为向量
review_embeddings = []
for review in reviews :
    review_embeddings.append(get_embedding(review))

# 计算余弦相似度
def cosin_similarity(vec_a, vec_b) :
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    cos_similarity = dot_product / (norm_a * norm_b)
    return cos_similarity

for i in range(len(reviews)): 
    print("第" + str(i) + "条评论为：" + reviews[i])
    pos_score = cosin_similarity(review_embeddings[i], positive)
    neg_score = cosin_similarity(review_embeddings[i], negative)
    print("与好评的相似度是：" + str(pos_score))
    print("与差评的相似度是" + str(neg_score))
    print("结果为" + "好评" if pos_score > neg_score
           else "差评")
    print("实际标签" + labels[i])
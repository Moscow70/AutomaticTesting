# 使用缓存能减少调用API的次数，显著降低费用，还能提升响应的速度

from langchain_community.cache import InMemoryCache
import time
from langchain_community.llms.baidu_qianfan_endpoint import QianfanLLMEndpoint
from langchain_core.globals import set_llm_cache

llm = QianfanLLMEndpoint(model= "ERNIE-Lite-8K")

set_llm_cache(InMemoryCache())

start_time = time.time()
result1 = llm.invoke("介绍手机如何恢复出厂设置")
print(result1)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"预测花费了{elapsed_time}秒。")

print("------------------------------------")
start_time = time.time()
result2 = llm.invoke("介绍手机如何恢复出厂设置")
print(result2)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"预测花费了{elapsed_time}秒。")
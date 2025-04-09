import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_framework_compatibility():
    # 测试平台支持的框架种类
    response = requests.get(f"{base_url}/frameworks")
    assert response.status_code == 200
    frameworks = response.json()
    assert "TensorFlow" in frameworks
    assert "PyTorch" in frameworks
    assert "JAX" in frameworks
    assert "PaddlePaddle" in frameworks

def test_framework_version_support():
    # 测试平台支持的框架版本范围
    response = requests.get(f"{base_url}/frameworks/versions")
    assert response.status_code == 200
    versions = response.json()
    assert "TensorFlow 1.x" in versions
    assert "TensorFlow 2.x" in versions
    assert "PyTorch 1.0-1.10" in versions

def test_framework_extension_support():
    # 测试平台是否支持特定框架的扩展库
    response = requests.get(f"{base_url}/frameworks/extensions")
    assert response.status_code == 200
    extensions = response.json()
    assert "TensorBoard" in extensions
    assert "PyTorch Lightning" in extensions

def test_community_image_support():
    # 测试平台是否支持社区镜像
    response = requests.get(f"{base_url}/community_images")
    assert response.status_code == 200
    images = response.json()
    assert "GitHub" in images
    assert "Docker Hub" in images
    assert "NVIDIA 开发者论坛" in images

def test_community_image_search():
    # 测试平台是否支持社区镜像搜索
    response = requests.get(f"{base_url}/community_images/search?name=GitHub")
    assert response.status_code == 200
    search_results = response.json()
    assert len(search_results) > 0

def test_pricing_and_billing():
    # 测试平台的价格透明度和计费模式
    response = requests.get(f"{base_url}/billing/info")
    assert response.status_code == 200
    billing_info = response.json()
    assert "充值方式" in billing_info
    assert "计费方式" in billing_info
    assert "扣费时机" in billing_info
    assert "功能弹性" in billing_info
    assert "关机处理" in billing_info

def test_model_training_performance_monitoring():
    # 测试模型训练性能监控维度
    response = requests.get(f"{base_url}/monitoring/dimensions")
    assert response.status_code == 200
    monitoring_dimensions = response.json()
    assert "资源利用率" in monitoring_dimensions
    assert "训练性能" in monitoring_dimensions
    assert "模型参数" in monitoring_dimensions
    assert "日志" in monitoring_dimensions
    assert "可视化" in monitoring_dimensions

def test_model_training_performance_granularity():
    # 测试模型训练性能监控粒度
    response = requests.get(f"{base_url}/monitoring/granularity")
    assert response.status_code == 200
    monitoring_granularity = response.json()
    assert "每10秒记录一次GPU的使用率" in monitoring_granularity
    assert "每轮训练结束后记录模型在训练集和验证集上的准确率" in monitoring_granularity
    assert "实时记录训练过程中异常事件" in monitoring_granularity
    assert "10s更新一次" in monitoring_granularity

def test_model_training_performance_configurability():
    # 测试模型训练性能监控可配置性
    response = requests.get(f"{base_url}/monitoring/config")
    assert response.status_code == 200
    monitoring_config = response.json()
    assert "监控频率" in monitoring_config
    assert "监控工具" in monitoring_config
    assert "日志路径" in monitoring_config
    assert "可视化工具" in monitoring_config
    assert "监控粒度" in monitoring_config
    assert "日志级别" in monitoring_config
    assert "日志文件格式" in monitoring_config
    assert "输出目录" in monitoring_config

if __name__ == "__main__":
    test_framework_compatibility()
    test_framework_version_support()
    test_framework_extension_support()
    test_community_image_support()
    test_community_image_search()
    test_pricing_and_billing()
    test_model_training_performance_monitoring()
    test_model_training_performance_granularity()
    test_model_training_performance_configurability()
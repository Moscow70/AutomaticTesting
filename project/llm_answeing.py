import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/login"

# 测试成功登录的情况
def test_successful_login():
    # 定义有效的用户名和密码
    payload = {
        "username": "user1",
        "password": "password1"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Login successful"}

# 测试无效用户名格式的情况
def test_invalid_username_format():
    # 定义无效的用户名格式（包含特殊字符）
    payload = {
        "username": "user!@#",
        "password": "password1"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"message": "Invalid username format"}

# 测试无效密码格式的情况
def test_invalid_password_format():
    # 定义无效的密码格式（长度不足）
    payload = {
        "username": "user1",
        "password": "pass"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"message": "Invalid password format"}

# 测试用户名或密码错误的情况
def test_invalid_credentials():
    # 定义错误的用户名和密码
    payload = {
        "username": "wronguser",
        "password": "wrongpass"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 401
    # 验证响应体
    assert response.json() == {"message": "Invalid credentials"}

# 运行所有测试
if __name__ == "__main__":
    test_successful_login()
    test_invalid_username_format()
    test_invalid_password_format()
    test_invalid_credentials()
    print("All tests passed!")

### 解释
# 1. **测试成功登录的情况**：
#    - 使用有效的用户名和密码发送POST请求，验证响应状态码为200，且响应体为`{"message": "Login successful"}`。

# 2. **测试无效用户名格式的情况**：
#    - 使用包含特殊字符的用户名发送POST请求，验证响应状态码为400，且响应体为`{"message": "Invalid username format"}`。

# 3. **测试无效密码格式的情况**：
#    - 使用长度不足的密码发送POST请求，验证响应状态码为400，且响应体为`{"message": "Invalid password format"}`。

# 4. **测试用户名或密码错误的情况**：
#    - 使用错误的用户名和密码发送POST请求，验证响应状态码为401，且响应体为`{"message": "Invalid credentials"}`。

# 5. **运行所有测试**：
#    - 在`__main__`块中运行所有测试函数，并在所有测试通过后打印`"All tests passed!"`。
import requests 
import json 

# 定义接口的基本URL
BASE_URL = "http://localhost:5000/login"

def test_successful_login(): 
    # 定义有效的用户名和密码
    payload = { 
        "username": "user1", 
        "password": "password1" 
    } 
    # 发送POST请求
    response = requests.post(BASE_URL, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Login successful"}

def test_invalid_username_format(): 
    # 定义无效的用户名
    payload = { 
        "username": "",  #空用户名
        "password": "password1" 
    } 
    # 发送POST请求
    response = requests.post(BASE_URL, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"message": "Invalid username format"}

def test_invalid_password_format(): 
    # 定义无效的密码
    payload = { 
        "username": "user1", 
        "password": ""  #空密码
    } 
    # 发送POST请求
    response = requests.post(BASE_URL, json=payload) 
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"message": "Invalid password format"}

def test_invalid_credentials(): 
    # 定义无效的用户名和密码
    payload = { 
        "username": "wrong_username", 
        "password": "wrong_password" 
    } 
    # 发送POST请求
    response = requests.post(BASE_URL, json=payload) 
    # 验证响应状态码
    assert response.status_code == 401
    # 验证响应体
    assert response.json() == {"message": "Invalid credentials"}

if __name__ == "__main__": 
    test_successful_login()
    test_invalid_username_format()
    test_invalid_password_format()
    test_invalid_credentials()
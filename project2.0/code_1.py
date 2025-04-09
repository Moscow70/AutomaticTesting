import requests
import json

# 定义接口的基本URL
base_url = "http://casc-stec.cn/api"

def test_successful_login():
    # 定义有效的用户名和密码
    payload = {
        "username": "user1",
        "password": "password1"
    }
    # 发送POST请求
    response = requests.post(base_url + "/login", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Login successful"}

def test_invalid_login():
    # 定义无效的用户名和密码
    payload = {
        "username": "invalidUser",
        "password": "wrongPassword"
    }
    # 发送POST请求
    response = requests.post(base_url + "/login", json=payload)
    # 验证响应状态码
    assert response.status_code == 401
    # 验证响应体
    assert response.json() == {"message": "Invalid credentials"}

def test_missing_credentials():
    # 定义缺少密码的请求
    payload = {
        "username": "user1"
    }
    # 发送POST请求
    response = requests.post(base_url + "/login", json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"message": "Missing credentials"}

if __name__ == "__main__":
    test_successful_login()
    test_invalid_login()
    test_missing_credentials()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_successful_login():
    # 定义有效的用户名和密码
    payload = {
        "username": "user1",
        "password": "password1"
    }
    # 发送POST请求到登录接口
    response = requests.post(f"{base_url}/login", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Login successful"}

def test_invalid_login():
    # 定义无效的用户名和密码
    payload = {
        "username": "invaliduser",
        "password": "invalidpassword"
    }
    # 发送POST请求到登录接口
    response = requests.post(f"{base_url}/login", json=payload)
    # 验证响应状态码
    assert response.status_code == 401
    # 验证响应体
    assert response.json() == {"message": "Invalid credentials"}

def test_logout():
    # 定义有效的用户名和密码
    payload = {
        "username": "user1",
        "password": "password1"
    }
    # 发送POST请求到登录接口
    login_response = requests.post(f"{base_url}/login", json=payload)
    # 获取登录后的token
    token = login_response.json().get("token")
    # 发送POST请求到注销接口
    logout_response = requests.post(f"{base_url}/logout", headers={"Authorization": f"Bearer {token}"})
    # 验证响应状态码
    assert logout_response.status_code == 200
    # 验证响应体
    assert logout_response.json() == {"message": "Logout successful"}

if __name__ == "__main__":
    test_successful_login()
    test_invalid_login()
    test_logout()

import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_get_purchase_contract_status():
    # 定义接口路径
    endpoint = "/purchase_contract_status"
    # 发送GET请求
    response = requests.get(base_url + endpoint)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert "contract_status" in response.json()

if __name__ == "__main__":
    test_get_purchase_contract_status()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_purchase_contract_management():
    # 测试采购合同管理接口
    endpoint = "/purchase_contract_management"
    payload = {
        "contract_id": "12345",
        "supplier_id": "67890",
        "amount": 10000
    }
    response = requests.post(base_url + endpoint, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Purchase contract management successful"}

def test_inbound_order_management():
    # 测试入库单管理接口
    endpoint = "/inbound_order_management"
    payload = {
        "order_id": "54321",
        "material_id": "09876",
        "quantity": 500
    }
    response = requests.post(base_url + endpoint, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Inbound order management successful"}

def test_outbound_order_management():
    # 测试出库单管理接口
    endpoint = "/outbound_order_management"
    payload = {
        "order_id": "11223",
        "material_id": "33445",
        "quantity": 300
    }
    response = requests.post(base_url + endpoint, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Outbound order management successful"}

def test_supplier_management():
    # 测试供应商管理接口
    endpoint = "/supplier_management"
    payload = {
        "supplier_id": "55667",
        "supplier_name": "Supplier A",
        "contact_info": "123-456-7890"
    }
    response = requests.post(base_url + endpoint, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Supplier management successful"}

def test_material_management():
    # 测试材料管理接口
    endpoint = "/material_management"
    payload = {
        "material_id": "77889",
        "material_name": "Material X",
        "unit": "kg"
    }
    response = requests.post(base_url + endpoint, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Material management successful"}

def test_inventory_management():
    # 测试库存管理接口
    endpoint = "/inventory_management"
    payload = {
        "inventory_id": "99001",
        "material_id": "11223",
        "quantity": 1000
    }
    response = requests.post(base_url + endpoint, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Inventory management successful"}

def test_inventory_warning():
    # 测试库存预警接口
    endpoint = "/inventory_warning"
    payload = {
        "material_id": "33445",
        "threshold": 50
    }
    response = requests.post(base_url + endpoint, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Inventory warning successful"}

def test_purchase_contract_approval():
    # 测试采购合同审批接口
    endpoint = "/purchase_contract_approval"
    payload = {
        "contract_id": "12345",
        "approver_id": "98765"
    }
    response = requests.post(base_url + endpoint, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Purchase contract approval successful"}

if __name__ == "__main__":
    test_purchase_contract_management()
    test_inbound_order_management()
    test_outbound_order_management()
    test_supplier_management()
    test_material_management()
    test_inventory_management()
    test_inventory_warning()
    test_purchase_contract_approval()

import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_approve_experiment_application():
    # 定义实验申请单审批的接口路径
    endpoint = "/approve_experiment_application"
    # 定义审批请求的payload
    payload = {
        "application_id": "12345",
        "approver": "admin",
        "status": "approved"
    }
    # 发送POST请求
    response = requests.post(base_url + endpoint, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Experiment application approved"}

def test_archive_experiment_application():
    # 定义实验单归档的接口路径
    endpoint = "/archive_experiment_application"
    # 定义归档请求的payload
    payload = {
        "application_id": "12345",
        "archiver": "admin"
    }
    # 发送POST请求
    response = requests.post(base_url + endpoint, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Experiment application archived"}

def test_return_materials_record():
    # 定义材料退还记录的接口路径
    endpoint = "/return_materials_record"
    # 定义退还材料请求的payload
    payload = {
        "application_id": "12345",
        "returner": "admin",
        "materials": ["material1", "material2"]
    }
    # 发送POST请求
    response = requests.post(base_url + endpoint, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Materials returned successfully"}

if __name__ == "__main__":
    test_approve_experiment_application()
    test_archive_experiment_application()
    test_return_materials_record()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_user_management():
    # 测试用户管理接口
    endpoint = "/user_management"
    url = base_url + endpoint
    payload = {
        "action": "create",
        "username": "new_user",
        "password": "new_password"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}

def test_role_view():
    # 测试角色查看接口
    endpoint = "/role_view"
    url = base_url + endpoint
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_department_management():
    # 测试部门管理接口
    endpoint = "/department_management"
    url = base_url + endpoint
    payload = {
        "action": "create",
        "department_name": "new_department"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Department created successfully"}

def test_log_management():
    # 测试日志管理接口
    endpoint = "/log_management"
    url = base_url + endpoint
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

if __name__ == "__main__":
    test_user_management()
    test_role_view()
    test_department_management()
    test_log_management()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/contract_management"

def test_create_contract():
    # 定义创建合同的有效数据
    payload = {
        "contract_id": "12345",
        "material": "实验材料A",
        "quantity": 100,
        "status": "pending"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/create_contract", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract created successfully"}

def test_approve_contract():
    # 定义审批合同的有效数据
    payload = {
        "contract_id": "12345",
        "status": "approved"
    }
    # 发送PUT请求
    response = requests.put(f"{base_url}/approve_contract", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract approved successfully"}

def test_reject_contract():
    # 定义拒绝合同的有效数据
    payload = {
        "contract_id": "12345",
        "status": "rejected"
    }
    # 发送PUT请求
    response = requests.put(f"{base_url}/reject_contract", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract rejected successfully"}

def test_fetch_contract():
    # 定义获取合同的有效数据
    contract_id = "12345"
    # 发送GET请求
    response = requests.get(f"{base_url}/fetch_contract/{contract_id}")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {
        "contract_id": "12345",
        "material": "实验材料A",
        "quantity": 100,
        "status": "approved"
    }

if __name__ == "__main__":
    test_create_contract()
    test_approve_contract()
    test_reject_contract()
    test_fetch_contract()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_contract_management():
    # 测试合同管理功能
    # 定义有效的合同数据
    payload = {
        "contract_type": "销售合同",
        "customer_id": "12345",
        "amount": "100000",
        "status": "draft"
    }
    # 发送POST请求创建合同
    response = requests.post(f"{base_url}/contract", json=payload)
    # 验证响应状态码
    assert response.status_code == 201
    # 验证响应体
    assert response.json()["message"] == "Contract created successfully"

def test_inventory_management():
    # 测试库存管理功能
    # 定义有效的入库单数据
    payload = {
        "material_id": "67890",
        "quantity": "50",
        "supplier_id": "98765"
    }
    # 发送POST请求创建入库单
    response = requests.post(f"{base_url}/inventory/inbound", json=payload)
    # 验证响应状态码
    assert response.status_code == 201
    # 验证响应体
    assert response.json()["message"] == "Inbound order created successfully"

def test_experiment_approval_management():
    # 测试实验审批管理功能
    # 定义有效的实验申请单数据
    payload = {
        "experiment_id": "54321",
        "material_id": "67890",
        "quantity": "10"
    }
    # 发送POST请求创建实验申请单
    response = requests.post(f"{base_url}/experiment/request", json=payload)
    # 验证响应状态码
    assert response.status_code == 201
    # 验证响应体
    assert response.json()["message"] == "Experiment request created successfully"

def test_system_management():
    # 测试系统管理功能
    # 定义有效的用户数据
    payload = {
        "username": "admin",
        "password": "admin123",
        "role": "admin"
    }
    # 发送POST请求创建用户
    response = requests.post(f"{base_url}/user", json=payload)
    # 验证响应状态码
    assert response.status_code == 201
    # 验证响应体
    assert response.json()["message"] == "User created successfully"

if __name__ == "__main__":
    test_contract_management()
    test_inventory_management()
    test_experiment_approval_management()
    test_system_management()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_experiment_submission_and_approval():
    # 实验员填写实验单并提交审批
    payload = {
        "experiment_details": "实验细节",
        "submitted_by": "实验员"
    }
    response = requests.post(f"{base_url}/submit_experiment", json=payload)
    assert response.status_code == 200
    experiment_id = response.json().get("experiment_id")

    # 安全员审批实验单
    approval_payload = {
        "experiment_id": experiment_id,
        "approved_by": "安全员",
        "status": "approved"
    }
    response = requests.post(f"{base_url}/approve_experiment", json=approval_payload)
    assert response.status_code == 200

    # 组长审批实验单
    approval_payload["approved_by"] = "组长"
    response = requests.post(f"{base_url}/approve_experiment", json=approval_payload)
    assert response.status_code == 200

    # 部门审批实验单
    approval_payload["approved_by"] = "部门"
    response = requests.post(f"{base_url}/approve_experiment", json=approval_payload)
    assert response.status_code == 200

def test_material_purchase_and_approval():
    # 库存管理员拟定采购合同
    payload = {
        "purchase_details": "采购细节",
        "submitted_by": "库存管理员"
    }
    response = requests.post(f"{base_url}/submit_purchase", json=payload)
    assert response.status_code == 200
    purchase_id = response.json().get("purchase_id")

    # 采购主管审批采购合同
    approval_payload = {
        "purchase_id": purchase_id,
        "approved_by": "采购主管",
        "status": "approved"
    }
    response = requests.post(f"{base_url}/approve_purchase", json=approval_payload)
    assert response.status_code == 200

    # 采购经理审批采购合同
    approval_payload["approved_by"] = "采购经理"
    response = requests.post(f"{base_url}/approve_purchase", json=approval_payload)
    assert response.status_code == 200

def test_experiment_report_archiving_and_approval():
    # 实验管理员填写归档单
    payload = {
        "report_details": "报告细节",
        "submitted_by": "实验管理员"
    }
    response = requests.post(f"{base_url}/submit_archive", json=payload)
    assert response.status_code == 200
    archive_id = response.json().get("archive_id")

    # 组长审批归档单
    approval_payload = {
        "archive_id": archive_id,
        "approved_by": "组长",
        "status": "approved"
    }
    response = requests.post(f"{base_url}/approve_archive", json=approval_payload)
    assert response.status_code == 200

    # 部门审批归档单
    approval_payload["approved_by"] = "部门"
    response = requests.post(f"{base_url}/approve_archive", json=approval_payload)
    assert response.status_code == 200

def test_sales_contract_generation_and_approval():
    # 合同管理员生成销售合同
    payload = {
        "contract_details": "合同细节",
        "submitted_by": "合同管理员"
    }
    response = requests.post(f"{base_url}/generate_sales_contract", json=payload)
    assert response.status_code == 200
    contract_id = response.json().get("contract_id")

    # 销售主管审批销售合同
    approval_payload = {
        "contract_id": contract_id,
        "approved_by": "销售主管",
        "status": "approved"
    }
    response = requests.post(f"{base_url}/approve_sales_contract", json=approval_payload)
    assert response.status_code == 200

    # 销售经理审批销售合同
    approval_payload["approved_by"] = "销售经理"
    response = requests.post(f"{base_url}/approve_sales_contract", json=approval_payload)
    assert response.status_code == 200

if __name__ == "__main__":
    test_experiment_submission_and_approval()
    test_material_purchase_and_approval()
    test_experiment_report_archiving_and_approval()
    test_sales_contract_generation_and_approval()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/login"

def test_successful_login():
    # 定义有效的用户名和密码
    payload = {
        "username": "admin",
        "password": "123456.aA"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Login successful"}

def test_invalid_login():
    # 定义无效的用户名和密码
    payload = {
        "username": "nonexistentuser",
        "password": "wrongpassword"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 401
    # 验证响应体
    assert response.json() == {"message": "用户名或密码错误"}

def test_frozen_user_login():
    # 定义冻结的用户名和密码
    payload = {
        "username": "frozenuser",
        "password": "password"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 403
    # 验证响应体
    assert response.json() == {"message": "用户已被冻结"}

def test_nonexistent_user_login():
    # 定义不存在的用户名和密码
    payload = {
        "username": "nonexistentuser",
        "password": "password"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 404
    # 验证响应体
    assert response.json() == {"message": "用户不存在"}

if __name__ == "__main__":
    test_successful_login()
    test_invalid_login()
    test_frozen_user_login()
    test_nonexistent_user_login()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/sales_contract"

def test_add_sales_contract():
    # 定义新增销售合同的数据
    payload = {
        "contract_number": "SC12345",
        "contract_name": "Test Contract",
        "department": "Sales",
        "contract_date": "2023-10-01",
        "contract_amount": 100000,
        "customer_name": "Test Customer",
        "payment_method": "Credit Card",
        "contract_status": "未提交"
    }
    # 发送POST请求
    response = requests.post(base_url + "/add", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract added successfully", "status": "未提交"}

def test_edit_sales_contract():
    # 定义编辑销售合同的数据
    payload = {
        "contract_number": "SC12345",
        "contract_name": "Updated Contract",
        "department": "Sales",
        "contract_date": "2023-10-01",
        "contract_amount": 120000,
        "customer_name": "Test Customer",
        "payment_method": "Bank Transfer",
        "contract_status": "未提交"
    }
    # 发送PUT请求
    response = requests.put(base_url + "/edit/SC12345", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract updated successfully", "status": "未提交"}

def test_submit_sales_contract():
    # 定义提交销售合同的数据
    payload = {
        "contract_number": "SC12345",
        "contract_status": "待销售主管审批"
    }
    # 发送POST请求
    response = requests.post(base_url + "/submit", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract submitted successfully", "status": "待销售主管审批"}

def test_delete_sales_contract():
    # 定义删除销售合同的数据
    payload = {
        "contract_number": "SC12345",
        "contract_status": "未提交"
    }
    # 发送DELETE请求
    response = requests.delete(base_url + "/delete/SC12345", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract deleted successfully"}

def test_query_sales_contract():
    # 定义查询销售合同的数据
    payload = {
        "contract_number": "SC12345"
    }
    # 发送GET请求
    response = requests.get(base_url + "/query", params=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"contract_number": "SC12345", "contract_name": "Updated Contract", "status": "未提交"}

if __name__ == "__main__":
    test_add_sales_contract()
    test_edit_sales_contract()
    test_submit_sales_contract()
    test_delete_sales_contract()
    test_query_sales_contract()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/sales_contract"

def test_delete_non_deletable_contract():
    # 定义一个一次性付款的销售合同编号
    contract_id = "HT-202405176119"
    # 发送DELETE请求
    response = requests.delete(f"{base_url}/{contract_id}")
    # 验证响应状态码，预期为400，因为一次性付款的销售合同不能删除
    assert response.status_code == 400
    # 验证响应体，预期返回错误信息
    assert response.json() == {"message": "Sales contract with one-time payment cannot be deleted"}

def test_query_contract_by_id():
    # 定义一个有效的合同编号
    contract_id = "HT-202405176119"
    # 发送GET请求
    response = requests.get(f"{base_url}?contract_id={contract_id}")
    # 验证响应状态码，预期为200
    assert response.status_code == 200
    # 验证响应体，预期返回合同信息
    assert "contract_id" in response.json()
    assert response.json()["contract_id"] == contract_id

def test_query_contract_by_department():
    # 定义一个有效的归属部门
    department = "Sales Department"
    # 发送GET请求
    response = requests.get(f"{base_url}?department={department}")
    # 验证响应状态码，预期为200
    assert response.status_code == 200
    # 验证响应体，预期返回合同信息列表
    assert isinstance(response.json(), list)
    for contract in response.json():
        assert "department" in contract
        assert contract["department"] == department

if __name__ == "__main__":
    test_delete_non_deletable_contract()
    test_query_contract_by_id()
    test_query_contract_by_department()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/api"

def test_valid_payment_conditions():
    # 定义有效的付款条件
    payload = {
        "payment_conditions": "现金支付",
        "payment_ratio": 50.00,
        "payment_amount": 500000.0000
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/payment", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Payment conditions accepted"}

def test_invalid_payment_ratio():
    # 定义无效的付款比例（超出范围）
    payload = {
        "payment_conditions": "现金支付",
        "payment_ratio": 101.00,
        "payment_amount": 500000.0000
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/payment", json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Invalid payment ratio"}

def test_invalid_payment_amount():
    # 定义无效的付款金额（手动修改）
    payload = {
        "payment_conditions": "现金支付",
        "payment_ratio": 50.00,
        "payment_amount": 600000.0000
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/payment", json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Payment amount cannot be manually modified"}

def test_valid_contract_info():
    # 定义有效的合同信息
    payload = {
        "contract_name": "销售合同",
        "contract_number": "CONTRACT-001",
        "contract_status": "Active",
        "contract_date": "2023-01-01",
        "department": "销售部",
        "customer_name": "客户A",
        "contract_amount": 1000000.00,
        "contact_person": "张三",
        "contact_number": "12345678901",
        "review_number": "REVIEW-001"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/contract", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract information accepted"}

def test_valid_experiment_info():
    # 定义有效的实验信息
    payload = {
        "experiment_name": "实验A",
        "contract_name": "销售合同",
        "applicant": "李四",
        "applicant_phone": "12345678901",
        "building_room": "1号楼-101",
        "safety_officer": "王五",
        "safety_officer_phone": "12345678901",
        "team_leader": "赵六",
        "team_leader_phone": "12345678901",
        "reaction_type": "化学反应",
        "reaction_temperature": 100,
        "reaction_pressure": 1.5,
        "reaction_medium": "水",
        "reaction_start_time": "2023-01-01",
        "reaction_end_time": "2023-01-02",
        "other_conditions": "无"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/experiment", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Experiment information accepted"}

if __name__ == "__main__":
    test_valid_payment_conditions()
    test_invalid_payment_ratio()
    test_invalid_payment_amount()
    test_valid_contract_info()
    test_valid_experiment_info()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/api"

def test_add_contract_invoice():
    # 定义新增合同发票的请求数据
    payload = {
        "contract_name": "合同A",
        "department": "销售部",
        "customer_name": "客户B",
        "invoice_number": "INV-001",
        "invoice_date": "2023-10-01",
        "invoice_amount": 10000.00,
        "invoice_staff": "张三"
    }
    
    # 发送POST请求
    response = requests.post(f"{base_url}/contract_invoices", json=payload)
    
    # 验证响应状态码
    assert response.status_code == 201
    
    # 验证响应体
    assert response.json() == {"message": "Contract invoice added successfully"}

def test_edit_contract_invoice():
    # 定义编辑合同发票的请求数据
    payload = {
        "invoice_amount": 12000.00,
        "invoice_staff": "李四"
    }
    
    # 发送PUT请求
    response = requests.put(f"{base_url}/contract_invoices/INV-001", json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Contract invoice updated successfully"}

def test_get_contract_invoice_details():
    # 发送GET请求
    response = requests.get(f"{base_url}/contract_invoices/INV-001")
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {
        "contract_name": "合同A",
        "department": "销售部",
        "customer_name": "客户B",
        "invoice_number": "INV-001",
        "invoice_date": "2023-10-01",
        "invoice_amount": 12000.00,
        "invoice_staff": "李四"
    }

def test_delete_contract_invoice():
    # 发送DELETE请求
    response = requests.delete(f"{base_url}/contract_invoices/INV-001")
    
    # 验证响应状态码
    assert response.status_code == 204

def test_query_contract_invoices():
    # 发送GET请求
    response = requests.get(f"{base_url}/contract_invoices")
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert isinstance(response.json(), list)

if __name__ == "__main__":
    test_add_contract_invoice()
    test_edit_contract_invoice()
    test_get_contract_invoice_details()
    test_delete_contract_invoice()
    test_query_contract_invoices()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/contract_invoice"

def test_add_contract_invoice():
    # 测试新增合同发票，开票金额为一次性付款
    payload = {
        "invoice_number": "FP-202405177957",
        "invoice_date": "2024-05-17",
        "contract_name": "合同A",
        "department": "部门A",
        "customer_name": "客户A",
        "invoice_amount": "一次性付款",
        "express_company": "顺丰",
        "express_number": "SF1234567890",
        "billing_staff": "张三",
        "attachment": "合同A.pdf"
    }
    response = requests.post(base_url, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Invoice added successfully"}

def test_add_contract_invoice_installment():
    # 测试新增合同发票，开票金额为首款（分期付款）
    payload = {
        "invoice_number": "FP-202405177958",
        "invoice_date": "2024-05-17",
        "contract_name": "合同B",
        "department": "部门B",
        "customer_name": "客户B",
        "invoice_amount": "首款",
        "express_company": "圆通",
        "express_number": "YT1234567890",
        "billing_staff": "李四",
        "attachment": "合同B.pdf"
    }
    response = requests.post(base_url, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Invoice added successfully"}

def test_edit_contract_invoice():
    # 测试编辑合同发票信息
    invoice_id = "FP-202405177957"
    payload = {
        "express_company": "中通",
        "express_number": "ZT1234567890"
    }
    response = requests.put(f"{base_url}/{invoice_id}", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Invoice updated successfully"}

def test_edit_contract_invoice_completed():
    # 测试编辑已履行完毕的合同发票信息（应失败）
    invoice_id = "FP-202405177958"
    payload = {
        "express_company": "申通",
        "express_number": "ST1234567890"
    }
    response = requests.put(f"{base_url}/{invoice_id}", json=payload)
    assert response.status_code == 400
    assert response.json() == {"message": "Invoice cannot be edited as it is completed"}

def test_view_contract_invoice_details():
    # 测试查看合同发票详情
    invoice_id = "FP-202405177957"
    response = requests.get(f"{base_url}/{invoice_id}")
    assert response.status_code == 200
    assert "invoice_number" in response.json()
    assert "contract_name" in response.json()
    assert "customer_name" in response.json()

def test_delete_contract_invoice():
    # 测试删除合同发票信息
    invoice_id = "FP-202405177957"
    response = requests.delete(f"{base_url}/{invoice_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Invoice deleted successfully"}

def test_delete_contract_invoice_completed():
    # 测试删除已履行完毕的合同发票信息（应失败）
    invoice_id = "FP-202405177958"
    response = requests.delete(f"{base_url}/{invoice_id}")
    assert response.status_code == 400
    assert response.json() == {"message": "Invoice cannot be deleted as it is completed"}

def test_query_contract_invoice():
    # 测试根据合同名称和客户名称模糊查询合同发票
    query_params = {
        "contract_name": "合同",
        "customer_name": "客户"
    }
    response = requests.get(base_url, params=query_params)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

if __name__ == "__main__":
    test_add_contract_invoice()
    test_add_contract_invoice_installment()
    test_edit_contract_invoice()
    test_edit_contract_invoice_completed()
    test_view_contract_invoice_details()
    test_delete_contract_invoice()
    test_delete_contract_invoice_completed()
    test_query_contract_invoice()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/contract"

def test_add_contract_payment():
    # 定义新增合同实际收款信息的有效数据
    payload = {
        "contract_name": "合同A",
        "payment_type": "一次性付款",
        "payment_date": "2024-05-17",
        "payment_condition": "全款",
        "payment_amount": 10000.00,
        "payment_percentage": 100.00
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/add_payment", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Payment added successfully"}

def test_edit_contract_payment():
    # 定义编辑合同实际收款信息的有效数据
    payload = {
        "payment_id": "HTSK-202405173142",
        "payment_date": "2024-05-18",
        "payment_condition": "部分付款"
    }
    # 发送PUT请求
    response = requests.put(f"{base_url}/edit_payment", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Payment updated successfully"}

def test_view_contract_payment_details():
    # 定义查看合同实际收款信息的有效数据
    payment_id = "HTSK-202405173142"
    # 发送GET请求
    response = requests.get(f"{base_url}/view_payment/{payment_id}")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {
        "payment_id": "HTSK-202405173142",
        "contract_name": "合同A",
        "payment_date": "2024-05-18",
        "payment_condition": "部分付款",
        "payment_amount": 10000.00,
        "payment_percentage": 100.00
    }

def test_delete_contract_payment():
    # 定义删除合同实际收款信息的有效数据
    payment_id = "HTSK-202405173142"
    # 发送DELETE请求
    response = requests.delete(f"{base_url}/delete_payment/{payment_id}")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Payment deleted successfully"}

def test_query_contract_payment():
    # 定义查询合同实际收款信息的有效数据
    query = {
        "contract_name": "合同A",
        "client_name": "客户B"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/query_payment", params=query)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == [
        {
            "payment_id": "HTSK-202405173142",
            "contract_name": "合同A",
            "client_name": "客户B",
            "payment_date": "2024-05-18",
            "payment_amount": 10000.00
        }
    ]

if __name__ == "__main__":
    test_add_contract_payment()
    test_edit_contract_payment()
    test_view_contract_payment_details()
    test_delete_contract_payment()
    test_query_contract_payment()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_create_sales_contract_with_installment_payment():
    # 定义分期付款的销售合同信息
    payload = {
        "payment_type": "installment",
        "payment_dates": ["2023-10-01", "2023-11-01"],
        "payment_conditions": ["initial payment", "final payment"],
        "payment_amounts": [50000.00, 50000.00],
        "payment_ratios": [50.00, 50.00]
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/sales_contract", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Sales contract created successfully"}

def test_create_sales_contract_with_full_payment():
    # 定义一次性付款的销售合同信息
    payload = {
        "payment_type": "full",
        "payment_date": "2023-10-01",
        "payment_amount": 100000.00,
        "payment_ratio": 100.00
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/sales_contract", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Sales contract created successfully"}

def test_view_experiment_details():
    # 定义实验单信息
    experiment_id = "exp123"
    # 发送GET请求
    response = requests.get(f"{base_url}/experiment/{experiment_id}")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["experiment_name"] == "Experiment 1"

def test_query_experiment_by_name():
    # 定义实验名称
    experiment_name = "Experiment 1"
    # 发送GET请求
    response = requests.get(f"{base_url}/experiment?name={experiment_name}")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert len(response.json()) > 0

def test_generate_sales_contract_from_experiment():
    # 定义实验单信息
    experiment_id = "exp123"
    # 发送POST请求
    response = requests.post(f"{base_url}/experiment/{experiment_id}/generate_contract")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Sales contract generated successfully"}

if __name__ == "__main__":
    test_create_sales_contract_with_installment_payment()
    test_create_sales_contract_with_full_payment()
    test_view_experiment_details()
    test_query_experiment_by_name()
    test_generate_sales_contract_from_experiment()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_contract_creation():
    # 定义合同信息
    payload = {
        "contract_name": "Test Contract",
        "contract_amount": 1000.50,
        "customer_name": "Test Customer",
        "contact_person": "John Doe",
        "contact_number": "1234567890"
    }
    # 发送POST请求创建合同
    response = requests.post(f"{base_url}/contract", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["message"] == "Contract created successfully"

def test_contract_modification():
    # 定义合同信息
    payload = {
        "contract_name": "Updated Contract",
        "contract_amount": 1500.75
    }
    # 发送PUT请求修改合同
    response = requests.put(f"{base_url}/contract/1", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["message"] == "Contract updated successfully"

def test_contract_deletion():
    # 发送DELETE请求删除合同
    response = requests.delete(f"{base_url}/contract/1")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["message"] == "Contract deleted successfully"

def test_attachment_upload():
    # 定义附件信息
    files = {'file': open('test_attachment.pdf', 'rb')}
    # 发送POST请求上传附件
    response = requests.post(f"{base_url}/contract/1/attachment", files=files)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["message"] == "Attachment uploaded successfully"

if __name__ == "__main__":
    test_contract_creation()
    test_contract_modification()
    test_contract_deletion()
    test_attachment_upload()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_add_customer():
    # 定义新增客户的信息
    payload = {
        "客户名称": "Test Customer",
        "归属部门": "研发部",
        "联系人": "张三",
        "联系电话": "13800138000",
        "联系地址": "北京市海淀区",
        "客户来源": "网络",
        "电子邮箱": "test@example.com"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/customers", json=payload)
    # 验证响应状态码
    assert response.status_code == 201
    # 验证响应体
    assert response.json()["客户名称"] == "Test Customer"

def test_edit_customer():
    # 定义编辑客户的信息
    payload = {
        "客户名称": "Updated Customer",
        "联系人": "李四",
        "联系电话": "13900139000",
        "联系地址": "上海市浦东新区"
    }
    # 发送PUT请求
    response = requests.put(f"{base_url}/customers/KH-202405174231", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["客户名称"] == "Updated Customer"

def test_get_customer_details():
    # 发送GET请求
    response = requests.get(f"{base_url}/customers/KH-202405174231")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["客户编号"] == "KH-202405174231"

def test_delete_customer():
    # 发送DELETE请求
    response = requests.delete(f"{base_url}/customers/KH-202405174231")
    # 验证响应状态码
    assert response.status_code == 204

def test_batch_delete_customers():
    # 定义批量删除的客户编号列表
    payload = ["KH-202405174232", "KH-202405174233"]
    # 发送DELETE请求
    response = requests.delete(f"{base_url}/customers/batch", json=payload)
    # 验证响应状态码
    assert response.status_code == 204

def test_search_customer():
    # 发送GET请求
    response = requests.get(f"{base_url}/customers?客户名称=Test")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert len(response.json()) > 0

if __name__ == "__main__":
    test_add_customer()
    test_edit_customer()
    test_get_customer_details()
    test_delete_customer()
    test_batch_delete_customers()
    test_search_customer()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/shipment"

def test_add_shipment_order():
    # 定义新增出货订单的请求体
    payload = {
        "shipmentOrderNumber": "CHDD-202405176298",
        "shipmentDate": "2024-05-17",
        "experimentName": "实验A",
        "department": "研发部",
        "customerName": "客户A",
        "consignee": "张三",
        "phoneNumber": "12345678901",
        "shippingAddress": "北京市海淀区",
        "operator": "李四"
    }
    # 发送POST请求
    response = requests.post(base_url + "/add", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Shipment order added successfully"}

def test_ship_existing_order():
    # 定义出货已存在的出货订单的请求体
    payload = {
        "shipmentOrderNumber": "CHDD-202405176298"
    }
    # 发送POST请求
    response = requests.post(base_url + "/ship", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Shipment completed successfully"}

def test_edit_unshipped_order():
    # 定义修改未出货订单的请求体
    payload = {
        "shipmentOrderNumber": "CHDD-202405176298",
        "shippingAddress": "上海市浦东新区"
    }
    # 发送PUT请求
    response = requests.put(base_url + "/edit", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Shipment order updated successfully"}

def test_view_shipment_order_details():
    # 定义查看出货订单详情的请求体
    payload = {
        "shipmentOrderNumber": "CHDD-202405176298"
    }
    # 发送GET请求
    response = requests.get(base_url + "/details", params=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert "shipmentOrderNumber" in response.json()

def test_delete_unshipped_order():
    # 定义删除未出货订单的请求体
    payload = {
        "shipmentOrderNumber": "CHDD-202405176298"
    }
    # 发送DELETE请求
    response = requests.delete(base_url + "/delete", params=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Shipment order deleted successfully"}

def test_query_shipment_order():
    # 定义查询出货订单的请求体
    payload = {
        "shipmentOrderNumber": "CHDD-202405176298"
    }
    # 发送GET请求
    response = requests.get(base_url + "/query", params=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert "shipmentOrderNumber" in response.json()

if __name__ == "__main__":
    test_add_shipment_order()
    test_ship_existing_order()
    test_edit_unshipped_order()
    test_view_shipment_order_details()
    test_delete_unshipped_order()
    test_query_shipment_order()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/api"

def test_auto_populate_experiment_info():
    # 定义测试数据
    payload = {
        "称": "实验名称",
        "合同名称": "合同名称",
        "申请人": "申请人",
        "申请人手机号": "12345678901",
        "楼号-房号": "1-101",
        "安全员": "安全员",
        "安全员手机": "12345678901",
        "组长": "组长",
        "组长手机": "12345678901",
        "反应类型": "类型1",
        "反应温度（℃）": "100",
        "反应压力（MPa）": "1.5",
        "反应介质": "介质1",
        "反应时间起": "2023-01-01",
        "反应时间止": "2023-01-02",
        "其他反应条件": "条件1",
        "通风橱能否停止": "是",
        "潜在危险": "危险1",
        "应急处置措施": "措施1",
        "危险等级": "等级1"
    }
    
    # 发送POST请求
    response = requests.post(base_url + "/experiment", json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Experiment information auto-populated successfully"}

def test_auto_populate_sales_contract_info():
    # 定义测试数据
    payload = {
        "合同名称": "合同名称",
        "合同编号": "编号123",
        "合同状态": "状态1",
        "合同日期": "2023-01-01",
        "归属部门": "部门1",
        "客户名称": "客户1",
        "合同金额（元）": "1000000.00",
        "联系人": "联系人1",
        "联系方式": "12345678901",
        "评审表编号": "编号123"
    }
    
    # 发送POST请求
    response = requests.post(base_url + "/sales-contract", json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Sales contract information auto-populated successfully"}

def test_auto_populate_material_info():
    # 定义测试数据
    payload = {
        "材料编号": "编号123",
        "材料名称": "材料1"
    }
    
    # 发送POST请求
    response = requests.post(base_url + "/material", json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Material information auto-populated successfully"}

if __name__ == "__main__":
    test_auto_populate_experiment_info()
    test_auto_populate_sales_contract_info()
    test_auto_populate_material_info()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_contract_approval():
    # 定义有效的合同审批信息
    payload = {
        "contract_number": "CNT12345",
        "contract_name": "Sample Contract",
        "department": "Sales",
        "contract_date": "2023-10-01",
        "contract_amount": 100000.00,
        "customer_name": "Sample Customer",
        "payment_method": "Credit Card",
        "contract_status": "Pending"
    }
    
    # 发送POST请求进行合同审批
    response = requests.post(f"{base_url}/contract/approve", json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Contract approved successfully"}

def test_contract_rejection():
    # 定义驳回的合同审批信息
    payload = {
        "contract_number": "CNT12345",
        "contract_name": "Sample Contract",
        "department": "Sales",
        "contract_date": "2023-10-01",
        "contract_amount": 100000.00,
        "customer_name": "Sample Customer",
        "payment_method": "Credit Card",
        "contract_status": "Pending",
        "rejection_reason": "Insufficient details"
    }
    
    # 发送POST请求进行合同驳回
    response = requests.post(f"{base_url}/contract/reject", json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Contract rejected", "status": "Rejected"}

def test_contract_query():
    # 定义查询参数
    params = {
        "contract_number": "CNT12345",
        "department": "Sales"
    }
    
    # 发送GET请求进行合同查询
    response = requests.get(f"{base_url}/contract/query", params=params)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == [
        {
            "contract_number": "CNT12345",
            "contract_name": "Sample Contract",
            "department": "Sales",
            "contract_date": "2023-10-01",
            "contract_amount": 100000.00,
            "customer_name": "Sample Customer",
            "payment_method": "Credit Card",
            "contract_status": "Pending"
        }
    ]

def test_contract_approval_history():
    # 定义查询参数
    params = {
        "approver": "SalesManager"
    }
    
    # 发送GET请求进行合同审批历史查询
    response = requests.get(f"{base_url}/contract/approval_history", params=params)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == [
        {
            "contract_number": "CNT12345",
            "contract_name": "Sample Contract",
            "department": "Sales",
            "contract_date": "2023-10-01",
            "contract_amount": 100000.00,
            "customer_name": "Sample Customer",
            "payment_method": "Credit Card",
            "contract_status": "Approved",
            "approver": "SalesManager"
        }
    ]

if __name__ == "__main__":
    test_contract_approval()
    test_contract_rejection()
    test_contract_query()
    test_contract_approval_history()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_contract_submission_within_one_day():
    # 定义合同信息，假设合同在当天提交
    payload = {
        "contract_number": "CONTRACT12345",
        "contract_date": "2023-10-01",
        "contract_name": "Sample Contract",
        "contract_amount": "100000.00",
        "payment_method": "Credit Card",
        "customer_name": "Customer A",
        "department": "Sales",
        "contact_person": "John Doe",
        "contact_number": "1234567890",
        "remarks": "This is a sample contract.",
        "review_number": "REVIEW12345"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/submit_contract", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体，假设返回一般消息
    assert response.json() == {"message": "一般消息"}

def test_contract_submission_after_one_day():
    # 定义合同信息，假设合同在超过一个自然日后提交
    payload = {
        "contract_number": "CONTRACT12346",
        "contract_date": "2023-09-30",
        "contract_name": "Sample Contract",
        "contract_amount": "100000.00",
        "payment_method": "Credit Card",
        "customer_name": "Customer A",
        "department": "Sales",
        "contact_person": "John Doe",
        "contact_number": "1234567890",
        "remarks": "This is a sample contract.",
        "review_number": "REVIEW12346"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/submit_contract", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体，假设返回重要消息
    assert response.json() == {"message": "重要消息"}

def test_contract_submission_after_two_days():
    # 定义合同信息，假设合同在超过两个自然日后提交
    payload = {
        "contract_number": "CONTRACT12347",
        "contract_date": "2023-09-29",
        "contract_name": "Sample Contract",
        "contract_amount": "100000.00",
        "payment_method": "Credit Card",
        "customer_name": "Customer A",
        "department": "Sales",
        "contact_person": "John Doe",
        "contact_number": "1234567890",
        "remarks": "This is a sample contract.",
        "review_number": "REVIEW12347"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/submit_contract", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体，假设返回紧急消息
    assert response.json() == {"message": "紧急消息"}

if __name__ == "__main__":
    test_contract_submission_within_one_day()
    test_contract_submission_after_one_day()
    test_contract_submission_after_two_days()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/purchase_contract"

def test_create_and_save_contract():
    # 定义新增采购合同的信息
    payload = {
        "合同编号": "CGHT-202405178703",
        "合同名称": "Test Contract",
        "评审表编号": "PR-20240517",
        "供应商": "Supplier A",
        "归属部门": "Department A",
        "合同金额": 10000.00,
        "合同日期": "2024-05-17"
    }
    # 发送POST请求新增合同
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体，合同状态应为【未提交】
    assert response.json().get("状态") == "未提交"

def test_submit_contract():
    # 定义提交采购合同的信息
    payload = {
        "合同编号": "CGHT-202405178703",
        "合同名称": "Test Contract",
        "评审表编号": "PR-20240517",
        "供应商": "Supplier A",
        "归属部门": "Department A",
        "合同金额": 10000.00,
        "合同日期": "2024-05-17"
    }
    # 发送POST请求提交合同
    response = requests.post(f"{base_url}/submit", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体，合同状态应为【待采购主管审批】
    assert response.json().get("状态") == "待采购主管审批"

def test_approve_contract_by_manager():
    # 定义采购经理审批通过的信息
    payload = {
        "合同编号": "CGHT-202405178703",
        "审批结果": "通过"
    }
    # 发送POST请求审批合同
    response = requests.post(f"{base_url}/approve", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体，合同状态应为【审批通过】
    assert response.json().get("状态") == "审批通过"

def test_reject_contract_by_manager():
    # 定义采购经理审批驳回的信息
    payload = {
        "合同编号": "CGHT-202405178703",
        "审批结果": "驳回"
    }
    # 发送POST请求审批合同
    response = requests.post(f"{base_url}/approve", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体，合同状态应为【审批未通过】
    assert response.json().get("状态") == "审批未通过"

def test_edit_and_resubmit_contract():
    # 定义编辑并重新提交采购合同的信息
    payload = {
        "合同编号": "CGHT-202405178703",
        "合同名称": "Updated Test Contract",
        "评审表编号": "PR-20240517",
        "供应商": "Supplier A",
        "归属部门": "Department A",
        "合同金额": 12000.00,
        "合同日期": "2024-05-17"
    }
    # 发送PUT请求编辑合同
    response = requests.put(f"{base_url}/edit", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体，合同状态应为【待采购主管审批】
    assert response.json().get("状态") == "待采购主管审批"

def test_delete_contract():
    # 定义删除采购合同的信息
    payload = {
        "合同编号": "CGHT-202405178703"
    }
    # 发送DELETE请求删除合同
    response = requests.delete(f"{base_url}/delete", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体，合同应被删除
    assert response.json().get("message") == "Contract deleted successfully"

def test_query_contract():
    # 定义查询采购合同的信息
    payload = {
        "合同编号": "CGHT-202405178703"
    }
    # 发送GET请求查询合同
    response = requests.get(f"{base_url}/query", params=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体，合同信息应正确返回
    assert response.json().get("合同编号") == "CGHT-202405178703"

if __name__ == "__main__":
    test_create_and_save_contract()
    test_submit_contract()
    test_approve_contract_by_manager()
    test_reject_contract_by_manager()
    test_edit_and_resubmit_contract()
    test_delete_contract()
    test_query_contract()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/warehouse"

def test_add_new_warehouse_order():
    # 定义新增入库单的请求数据
    payload = {
        "入库单编号": "RKD-202405178476",
        "入库单日期": "2024-05-17",
        "合同名称": "合同A",
        "归属部门": "部门A",
        "入库检验员": "检验员A",
        "到货位置": "位置A",
        "材料信息": [
            {
                "材料编号": "材料1",
                "材料名称": "材料A",
                "单价（元）": 100.50,
                "数量": 5,
                "待入库数量": 10,
                "计量单位": "枚",
                "是否免检": "是"
            }
        ]
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/add", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "入库单新增成功"}

def test_view_warehouse_order_details():
    # 定义查看入库单详情的请求数据
    order_id = "RKD-202405178476"
    # 发送GET请求
    response = requests.get(f"{base_url}/details/{order_id}")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["入库单编号"] == order_id

def test_qualify_inspection():
    # 定义质检合格的请求数据
    order_id = "RKD-202405178476"
    material_id = "材料1"
    payload = {
        "质检编号": "质检123"
    }
    # 发送PUT请求
    response = requests.put(f"{base_url}/qualify/{order_id}/{material_id}", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "质检合格，材料已入库"}

def test_query_warehouse_orders():
    # 定义查询入库单的请求数据
    query_params = {
        "入库单编号": "RKD-202405178476",
        "入库日期": "2024-05-17",
        "合同名称": "合同A"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/query", params=query_params)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()[0]["入库单编号"] == "RKD-202405178476"

if __name__ == "__main__":
    test_add_new_warehouse_order()
    test_view_warehouse_order_details()
    test_qualify_inspection()
    test_query_warehouse_orders()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/api"

def test_add_outbound_order():
    # 定义出库单信息
    payload = {
        "outbound_order_number": "CKD-202405175997",
        "outbound_date": "2024-05-17",
        "experiment_order": "审批通过",
        "department": "研发部",
        "material_person": "张三",
        "outbound_type": "实验",
        "handler": "李四"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/outbound", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Outbound order added successfully"}

def test_view_outbound_order_details():
    # 定义出库单编号
    outbound_order_number = "CKD-202405175997"
    # 发送GET请求
    response = requests.get(f"{base_url}/outbound/{outbound_order_number}")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {
        "outbound_order_number": "CKD-202405175997",
        "outbound_date": "2024-05-17",
        "experiment_order": "审批通过",
        "department": "研发部",
        "material_person": "张三",
        "outbound_type": "实验",
        "handler": "李四"
    }

def test_query_outbound_orders():
    # 定义查询参数
    params = {
        "outbound_date": "2024-05-17",
        "material_person": "张三"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/outbound", params=params)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == [
        {
            "outbound_order_number": "CKD-202405175997",
            "outbound_date": "2024-05-17",
            "experiment_order": "审批通过",
            "department": "研发部",
            "material_person": "张三",
            "outbound_type": "实验",
            "handler": "李四"
        }
    ]

if __name__ == "__main__":
    test_add_outbound_order()
    test_view_outbound_order_details()
    test_query_outbound_orders()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/suppliers"

def test_add_supplier():
    # 定义新增供应商的请求数据
    payload = {
        "供应商名称": "Test Supplier",
        "归属部门": "Test Department",
        "联系人": "Test Contact",
        "联系电话": "13800138000",
        "联系地址": "Test Address",
        "电子邮箱": "test@example.com",
        "供货周期": "7 days",
        "供应商资质": "test_document.pdf",
        "备注": "Test Supplier Note"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 201
    # 验证响应体
    assert response.json()["供应商名称"] == "Test Supplier"

def test_edit_supplier():
    # 定义编辑供应商的请求数据
    payload = {
        "供应商名称": "Updated Supplier",
        "归属部门": "Updated Department",
        "联系人": "Updated Contact",
        "联系电话": "13800138001",
        "联系地址": "Updated Address",
        "电子邮箱": "updated@example.com",
        "供货周期": "10 days",
        "供应商资质": "updated_document.pdf",
        "备注": "Updated Supplier Note"
    }
    # 发送PUT请求
    response = requests.put(f"{base_url}/1", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["供应商名称"] == "Updated Supplier"

def test_get_supplier_details():
    # 发送GET请求
    response = requests.get(f"{base_url}/1")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["供应商编号"] == "GYS-202405172616"

def test_delete_supplier():
    # 发送DELETE请求
    response = requests.delete(f"{base_url}/1")
    # 验证响应状态码
    assert response.status_code == 204

def test_batch_delete_suppliers():
    # 定义批量删除供应商的请求数据
    payload = {
        "供应商编号列表": ["GYS-202405172616", "GYS-202405172617"]
    }
    # 发送DELETE请求
    response = requests.delete(f"{base_url}/batch", json=payload)
    # 验证响应状态码
    assert response.status_code == 204

def test_query_suppliers():
    # 定义查询供应商的请求数据
    params = {
        "供应商名称": "Test Supplier",
        "联系人": "Test Contact",
        "联系电话": "13800138000"
    }
    # 发送GET请求
    response = requests.get(base_url, params=params)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert len(response.json()) > 0

if __name__ == "__main__":
    test_add_supplier()
    test_edit_supplier()
    test_get_supplier_details()
    test_delete_supplier()
    test_batch_delete_suppliers()
    test_query_suppliers()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/materials"

def test_add_material():
    # 定义新增材料的payload
    payload = {
        "材料编号": "PC-202405173910",
        "材料名称": "测试材料",
        "计量单位": "个",
        "采购价格": 100.00,
        "是否免检": "免检",
        "材料描述": "测试材料描述",
        "备注": "测试材料备注",
        "材料图片": "test_image.png"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/add", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Material added successfully"}

def test_edit_material():
    # 定义编辑材料的payload
    payload = {
        "材料编号": "PC-202405173910",
        "材料名称": "更新材料",
        "计量单位": "KG",
        "采购价格": 150.00,
        "是否免检": "不免检",
        "材料描述": "更新材料描述",
        "备注": "更新材料备注"
    }
    # 发送PUT请求
    response = requests.put(f"{base_url}/edit/PC-202405173910", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Material updated successfully"}

def test_get_material_details():
    # 发送GET请求
    response = requests.get(f"{base_url}/details/PC-202405173910")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["材料编号"] == "PC-202405173910"

def test_delete_material():
    # 发送DELETE请求
    response = requests.delete(f"{base_url}/delete/PC-202405173910")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Material deleted successfully"}

def test_batch_delete_materials():
    # 定义批量删除材料的payload
    payload = {
        "材料编号列表": ["PC-202405173910", "PC-202405173911"]
    }
    # 发送DELETE请求
    response = requests.delete(f"{base_url}/batch_delete", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Materials deleted successfully"}

def test_view_material_records():
    # 发送GET请求
    response = requests.get(f"{base_url}/records/PC-202405173910")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["材料编号"] == "PC-202405173910"

def test_search_materials():
    # 定义搜索材料的payload
    payload = {
        "材料编号": "PC-202405173910",
        "材料名称": "测试材料",
        "是否免检": "免检"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/search", params=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()[0]["材料编号"] == "PC-202405173910"

if __name__ == "__main__":
    test_add_material()
    test_edit_material()
    test_get_material_details()
    test_delete_material()
    test_batch_delete_materials()
    test_view_material_records()
    test_search_materials()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/inventory"

def test_successful_inventory_increase():
    # 定义盘赢操作的请求体
    payload = {
        "material_id": "MAT001",
        "material_name": "Material A",
        "quantity": 10,
        "unit": "pcs",
        "increase_quantity": 5
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/increase", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Inventory increased successfully"}

def test_successful_inventory_decrease():
    # 定义盘亏操作的请求体
    payload = {
        "material_id": "MAT001",
        "material_name": "Material A",
        "quantity": 10,
        "unit": "pcs",
        "decrease_quantity": 3
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/decrease", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Inventory decreased successfully"}

def test_inventory_detail_query():
    # 定义查询盘库明细的请求体
    payload = {
        "material_id": "MAT001",
        "material_name": "Material A"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/detail", params=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert "operation_date" in response.json()
    assert "type" in response.json()
    assert "quantity" in response.json()
    assert "description" in response.json()

def test_inventory_query():
    # 定义查询库存的请求体
    payload = {
        "material_id": "MAT001",
        "material_name": "Material A"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/query", params=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert "material_id" in response.json()
    assert "material_name" in response.json()
    assert "quantity" in response.json()
    assert "unit" in response.json()

if __name__ == "__main__":
    test_successful_inventory_increase()
    test_successful_inventory_decrease()
    test_inventory_detail_query()
    test_inventory_query()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_inventory_update():
    # 测试库存数量的更新
    payload = {
        "action": "update_inventory",
        "material_id": "12345",
        "quantity": 50
    }
    response = requests.post(f"{base_url}/inventory", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Inventory updated successfully"

def test_inventory_alert():
    # 测试库存预警
    payload = {
        "action": "check_alert",
        "material_id": "12345",
        "quantity": 5
    }
    response = requests.post(f"{base_url}/inventory/alert", json=payload)
    assert response.status_code == 200
    assert response.json()["alert"] == "Replenishment needed"

def test_purchase_contract_approval():
    # 测试采购合同审批
    payload = {
        "action": "approve_contract",
        "contract_id": "C12345",
        "approver": "Manager"
    }
    response = requests.post(f"{base_url}/purchase/approve", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "Approved"

def test_purchase_contract_query():
    # 测试采购合同查询
    payload = {
        "action": "query_contract",
        "contract_id": "C12345"
    }
    response = requests.post(f"{base_url}/purchase/query", json=payload)
    assert response.status_code == 200
    assert response.json()["contract_id"] == "C12345"

if __name__ == "__main__":
    test_inventory_update()
    test_inventory_alert()
    test_purchase_contract_approval()
    test_purchase_contract_query()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/api"

def test_submit_experiment_application():
    # 实验员提交实验申请单
    payload = {
        "action": "submit",
        "status": "未提交"
    }
    response = requests.post(f"{base_url}/experiment/application", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "待安全员审批"

def test_security_officer_approve():
    # 安全员审批通过
    payload = {
        "action": "approve",
        "status": "待安全员审批"
    }
    response = requests.post(f"{base_url}/experiment/application/security", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "待组长审批"

def test_team_leader_reject():
    # 组长驳回
    payload = {
        "action": "reject",
        "status": "待组长审批"
    }
    response = requests.post(f"{base_url}/experiment/application/leader", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "组长退回"

def test_department_approve():
    # 部门审批通过
    payload = {
        "action": "approve",
        "status": "待部门审批"
    }
    response = requests.post(f"{base_url}/experiment/application/department", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "审批通过"

def test_archive_approval_failure():
    # 归档单审批未通过
    payload = {
        "action": "reject",
        "status": "待部门审批"
    }
    response = requests.post(f"{base_url}/experiment/archive", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "审批未通过"

if __name__ == "__main__":
    test_submit_experiment_application()
    test_security_officer_approve()
    test_team_leader_reject()
    test_department_approve()
    test_archive_approval_failure()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/experiment"

def test_add_experiment():
    # 定义新增实验申请单的请求体
    payload = {
        "实验名称": "实验1",
        "合同名称": "合同1",
        "申请人": "实验员1",
        "申请人手机号": "12345678901",
        "楼号-房号": "1-1",
        "安全员": "安全员1",
        "安全员手机": "12345678901",
        "组长": "组长1",
        "组长手机": "12345678901",
        "反应类型": ["氯化反应", "硝化反应"],
        "反应温度": 25,
        "反应压力": 1.5,
        "反应时间起": "2023-10-01T00:00:00",
        "反应时间止": "2023-10-01T01:00:00"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/add", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Experiment added successfully"}

def test_save_experiment():
    # 定义暂存实验申请单的请求体
    payload = {
        "实验名称": "实验1"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/save", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Experiment saved successfully", "审批状态": "未提交"}

def test_submit_experiment():
    # 定义提交实验申请单的请求体
    payload = {
        "实验名称": "实验1"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/submit", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Experiment submitted successfully", "审批状态": "待安全员审批"}

def test_edit_experiment():
    # 定义编辑实验申请单的请求体
    payload = {
        "实验名称": "实验1",
        "反应温度": 30
    }
    # 发送PUT请求
    response = requests.put(f"{base_url}/edit", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Experiment edited successfully", "审批状态": "待安全员审批"}

def test_view_experiment_details():
    # 定义查看实验申请单详情的请求体
    payload = {
        "实验名称": "实验1"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/details", params=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["实验名称"] == "实验1"

def test_delete_experiment():
    # 定义删除实验申请单的请求体
    payload = {
        "实验名称": "实验1"
    }
    # 发送DELETE请求
    response = requests.delete(f"{base_url}/delete", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Experiment deleted successfully"}

def test_query_experiment():
    # 定义查询实验申请单的请求体
    payload = {
        "实验名称": "实验"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/query", params=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["实验名称"] == "实验1"

def test_start_experiment():
    # 定义开始实验的请求体
    payload = {
        "实验名称": "实验1"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/start", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Experiment started successfully", "实验状态": "实验中"}

if __name__ == "__main__":
    test_add_experiment()
    test_save_experiment()
    test_submit_experiment()
    test_edit_experiment()
    test_view_experiment_details()
    test_delete_experiment()
    test_query_experiment()
    test_start_experiment()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/lab"

def test_valid_reaction_input():
    # 定义有效的反应输入
    payload = {
        "reaction_type": "氧化反应",
        "reaction_temperature": 90,
        "reaction_pressure": 0.3,
        "reaction_medium": "水",
        "reaction_time_start": "2023-10-01 08:00:00",
        "reaction_time_end": "2023-10-01 10:00:00",
        "ventilation_stop": "否",
        "potential_hazards": ["燃烧", "中毒"],
        "emergency_measures": ["灭火器", "通风"]
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Reaction input successful"}

def test_invalid_temperature():
    # 定义无效的反应温度
    payload = {
        "reaction_type": "氧化反应",
        "reaction_temperature": 110,
        "reaction_pressure": 0.3,
        "reaction_medium": "水",
        "reaction_time_start": "2023-10-01 08:00:00",
        "reaction_time_end": "2023-10-01 10:00:00",
        "ventilation_stop": "否",
        "potential_hazards": ["燃烧", "中毒"],
        "emergency_measures": ["灭火器", "通风"]
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Temperature exceeds 100℃"}

def test_invalid_pressure():
    # 定义无效的反应压力
    payload = {
        "reaction_type": "氧化反应",
        "reaction_temperature": 90,
        "reaction_pressure": 0.5,
        "reaction_medium": "水",
        "reaction_time_start": "2023-10-01 08:00:00",
        "reaction_time_end": "2023-10-01 10:00:00",
        "ventilation_stop": "否",
        "potential_hazards": ["燃烧", "中毒"],
        "emergency_measures": ["灭火器", "通风"]
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Pressure exceeds 0.4MPa"}

def test_missing_required_field():
    # 定义缺少必填字段的输入
    payload = {
        "reaction_type": "氧化反应",
        "reaction_temperature": 90,
        "reaction_pressure": 0.3,
        "reaction_medium": "水",
        "reaction_time_start": "2023-10-01 08:00:00",
        "reaction_time_end": "2023-10-01 10:00:00",
        "potential_hazards": ["燃烧", "中毒"],
        "emergency_measures": ["灭火器", "通风"]
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Missing required field: ventilation_stop"}

if __name__ == "__main__":
    test_valid_reaction_input()
    test_invalid_temperature()
    test_invalid_pressure()
    test_missing_required_field()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/archive"

def test_add_archive():
    # 定义新增归档单的请求数据
    payload = {
        "实验名称": "实验完成",
        "归档编号": "unique_archive_number_123",
        "归档日期": "2023-10-01",
        "安全注意事项": "注意安全",
        "存在的问题与不足": "无",
        "备注": "无"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "归档单新增成功"}

def test_save_archive():
    # 定义暂存归档单的请求数据
    payload = {
        "实验名称": "实验完成",
        "归档编号": "unique_archive_number_123",
        "归档日期": "2023-10-01",
        "安全注意事项": "注意安全",
        "存在的问题与不足": "无",
        "备注": "无"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/save", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "归档单暂存成功", "status": "未提交"}

def test_submit_archive():
    # 定义提交归档单的请求数据
    payload = {
        "实验名称": "实验完成",
        "归档编号": "unique_archive_number_123",
        "归档日期": "2023-10-01",
        "安全注意事项": "注意安全",
        "存在的问题与不足": "无",
        "备注": "无"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/submit", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "归档单提交成功", "status": "待组长审批"}

def test_edit_archive():
    # 定义编辑归档单的请求数据
    payload = {
        "实验名称": "实验完成",
        "归档编号": "unique_archive_number_123",
        "归档日期": "2023-10-01",
        "安全注意事项": "注意安全",
        "存在的问题与不足": "无",
        "备注": "无"
    }
    # 发送PUT请求
    response = requests.put(f"{base_url}/edit", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "归档单编辑成功", "status": "待组长审批"}

def test_delete_archive():
    # 定义删除归档单的请求数据
    payload = {
        "归档编号": "unique_archive_number_123"
    }
    # 发送DELETE请求
    response = requests.delete(f"{base_url}/delete", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "归档单删除成功"}

def test_query_archive():
    # 定义查询归档单的请求数据
    payload = {
        "归档编号": "unique_archive_number_123",
        "归档日期": "2023-10-01"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/query", params=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "查询成功", "data": [{"归档编号": "unique_archive_number_123", "归档日期": "2023-10-01"}]}

def test_export_archive():
    # 定义导出归档单的请求数据
    payload = {
        "归档编号": "unique_archive_number_123"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/export", params=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.headers["Content-Type"] == "application/json"
    assert response.json() == {"message": "导出成功", "data": [{"归档编号": "unique_archive_number_123", "归档日期": "2023-10-01"}]}

if __name__ == "__main__":
    test_add_archive()
    test_save_archive()
    test_submit_archive()
    test_edit_archive()
    test_delete_archive()
    test_query_archive()
    test_export_archive()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/experiment"

def test_auto_populate_experiment_info():
    # 定义实验单信息
    payload = {
        "安全员手机": "12345678901",
        "组长": "张三",
        "组长手机": "12345678901",
        "反应类型": "类型A",
        "反应温度（℃）": 100,
        "反应压力（MPa）": 1.5,
        "反应介质": "水",
        "反应时间起": "2023-10-01",
        "反应时间止": "2023-10-02",
        "其他反应条件": "无",
        "通风橱能否停止": "是",
        "潜在危险": "无",
        "应急处置措施": "无",
        "危险等级": "低"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Experiment info auto-populated successfully"}

def test_auto_populate_material_info():
    # 定义实验材料信息
    payload = {
        "材料编号": "MAT12345678901234567890",
        "材料名称": "材料A",
        "单价（元）": 12345.67,
        "数量": 100,
        "计量单位": "个",
        "是否免检": "否"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Material info auto-populated successfully"}

def test_auto_populate_archive_info():
    # 定义归档单信息
    payload = {
        "归档编号": "ARC12345678901234567890",
        "归档日期": "2023-10-01",
        "归档人": "李四",
        "安全注意事项": "注意防火",
        "存在的问题与不足": "无",
        "备注": "无",
        "实验名称": "实验A"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Archive info auto-populated successfully"}

if __name__ == "__main__":
    test_auto_populate_experiment_info()
    test_auto_populate_material_info()
    test_auto_populate_archive_info()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_auto_fill_experiment_info():
    # 定义实验单信息
    payload = {
        "安全员手机": "12345678901",
        "组长": "组长姓名",
        "组长手机": "12345678901",
        "实验材料": "材料A",
        "反应类型": "类型A",
        "反应温度（℃）": 50,
        "反应压力（MPa）": 1.5,
        "反应介质": "介质A",
        "反应时间（h）": "2023-10-01T12:00:00Z",
        "其他反应条件": "条件A",
        "通风橱能否停止": "是",
        "潜在危险": "危险A",
        "应急处置措施": "措施A",
        "组长意见": "同意",
        "部门意见": "批准"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/experiment", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Experiment info auto-filled successfully"}

def test_query_material_return_records():
    # 定义查询条件
    query = {
        "材料名称": "材料A",
        "材料编号": "12345678901234567890"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/material/return", params=query)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Material return records found"}

def test_view_experiment_details():
    # 定义实验单编号
    experiment_id = "12345"
    # 发送GET请求
    response = requests.get(f"{base_url}/experiment/{experiment_id}")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Experiment details found"}

if __name__ == "__main__":
    test_auto_fill_experiment_info()
    test_query_material_return_records()
    test_view_experiment_details()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/experiment"

def test_add_experiment_info():
    # 定义实验单信息
    payload = {
        "组长": "张三",
        "组长手机": "13800138000",
        "反应类型": "类型A",
        "反应温度（℃）": 25,
        "反应压力（MPa）": 1.5,
        "反应介质": "介质A",
        "反应时间起": "2023-10-01",
        "反应时间止": "2023-10-05",
        "其他反应条件": "条件A",
        "通风橱能否停止": "是",
        "潜在危险": "无",
        "应急处置措施": "措施A",
        "危险等级": "低"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Experiment info added successfully"}

def test_add_material_info():
    # 定义实验材料信息
    payload = {
        "材料编号": "MAT001",
        "材料名称": "材料A",
        "单价（元）": 100.50,
        "数量": 10,
        "计量单位": "个",
        "是否免检": "否"
    }
    # 发送POST请求
    response = requests.post(base_url + "/material", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Material info added successfully"}

def test_add_building_info():
    # 定义楼号房号信息
    payload = {
        "楼号": 1,
        "房号": 101,
        "安全员": "李四",
        "安全员手机号": "13900139000",
        "组长": "张三",
        "组长手机号": "13800138000",
        "备注": "备注信息"
    }
    # 发送POST请求
    response = requests.post(base_url + "/building", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Building info added successfully"}

def test_edit_building_info():
    # 定义楼号房号信息
    payload = {
        "楼号": 1,
        "房号": 101,
        "安全员": "王五",
        "安全员手机号": "13700137000",
        "组长": "张三",
        "组长手机号": "13800138000",
        "备注": "备注信息"
    }
    # 发送PUT请求
    response = requests.put(base_url + "/building/1/101", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Building info updated successfully"}

def test_delete_building_info():
    # 发送DELETE请求
    response = requests.delete(base_url + "/building/1/101")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Building info deleted successfully"}

def test_query_building_info():
    # 发送GET请求
    response = requests.get(base_url + "/building?楼号=1&房号=101")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"楼号": 1, "房号": 101, "安全员": "王五", "安全员手机号": "13700137000", "组长": "张三", "组长手机号": "13800138000", "备注": "备注信息"}

if __name__ == "__main__":
    test_add_experiment_info()
    test_add_material_info()
    test_add_building_info()
    test_edit_building_info()
    test_delete_building_info()
    test_query_building_info()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/approve"

def test_approve_experiment_single():
    # 定义有效的审批请求数据
    payload = {
        "security_officer": "安全员1",
        "security_officer_phone": "13800138000",
        "leader": "组长1",
        "leader_phone": "13900139000",
        "remarks": "实验备注",
        "experiment_name": "实验名称",
        "applicant": "申请人",
        "building_room": "楼号-房号",
        "reaction_temperature": "25",
        "reaction_pressure": "1.0",
        "reaction_type": "反应类型",
        "reaction_time_start": "2023-10-01T00:00:00",
        "reaction_time_end": "2023-10-01T01:00:00",
        "approval_status": "待审批",
        "experiment_status": "进行中"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Experiment single approved successfully"}

def test_query_experiment_single():
    # 定义查询请求数据
    query_params = {
        "experiment_name": "实验名称"
    }
    
    # 发送GET请求
    response = requests.get(base_url, params=query_params)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == [
        {
            "experiment_name": "实验名称",
            "applicant": "申请人",
            "building_room": "楼号-房号",
            "reaction_temperature": "25",
            "reaction_pressure": "1.0",
            "reaction_type": "反应类型",
            "reaction_time_start": "2023-10-01T00:00:00",
            "reaction_time_end": "2023-10-01T01:00:00",
            "approval_status": "待审批",
            "experiment_status": "进行中"
        }
    ]

def test_view_approval_history():
    # 发送GET请求查看审批历史
    response = requests.get(f"{base_url}/history")
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == [
        {
            "experiment_name": "实验名称",
            "applicant": "申请人",
            "building_room": "楼号-房号",
            "reaction_temperature": "25",
            "reaction_pressure": "1.0",
            "reaction_type": "反应类型",
            "reaction_time_start": "2023-10-01T00:00:00",
            "reaction_time_end": "2023-10-01T01:00:00",
            "approval_status": "已审批",
            "experiment_status": "已完成"
        }
    ]

if __name__ == "__main__":
    test_approve_experiment_single()
    test_query_experiment_single()
    test_view_approval_history()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/experiment"

def test_auto_populate_experiment_info():
    # 定义实验单信息
    payload = {
        "实验名称": "实验1",
        "归属部门": "部门A",
        "申请人": "申请人A",
        "申请人手机号": "12345678901",
        "楼号-房号": "1-101",
        "安全员": "安全员A",
        "安全员手机": "12345678901",
        "组长": "组长A",
        "组长手机": "12345678901",
        "反应类型": "类型A",
        "反应温度（℃）": 25,
        "反应压力（MPa）": 1.5,
        "反应介质": "介质A",
        "反应时间起-止": "2023-01-01至2023-01-02",
        "其他反应条件": "条件A",
        "通风橱能否停止": "是",
        "潜在危险": "危险A",
        "应急处置措施": "措施A",
        "危险等级": "等级A"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Experiment information auto-populated successfully"}

if __name__ == "__main__":
    test_auto_populate_experiment_info()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/archive"

def test_archive_approval():
    # 定义归档审批的请求数据
    payload = {
        "experiment_name": "实验名称",
        "archive_number": "归档编号",
        "archive_date": "2023-10-01",
        "archiver": "归档人",
        "safety_notes": "安全注意事项",
        "issues_and_shortcomings": "存在的问题与不足",
        "remarks": "备注",
        "archive_status": "归档状态"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Archive approval successful"}

def test_batch_approval_pass():
    # 定义批量审批通过的请求数据
    payload = {
        "action": "batch_pass",
        "archive_numbers": ["归档编号1", "归档编号2"]
    }
    
    # 发送POST请求
    response = requests.post(base_url + "/batch", json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Batch approval pass successful"}

def test_batch_approval_reject():
    # 定义批量审批驳回的请求数据
    payload = {
        "action": "batch_reject",
        "archive_numbers": ["归档编号3", "归档编号4"]
    }
    
    # 发送POST请求
    response = requests.post(base_url + "/batch", json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Batch approval reject successful"}

def test_query_archive():
    # 定义查询归档单的请求数据
    payload = {
        "archive_number": "归档编号",
        "archive_date": "2023-10-01"
    }
    
    # 发送GET请求
    response = requests.get(base_url + "/query", params=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Query successful", "data": [{"archive_number": "归档编号", "archive_date": "2023-10-01"}]}

def test_approval_history():
    # 发送GET请求获取审批历史
    response = requests.get(base_url + "/history")
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Approval history retrieved", "data": [{"archive_number": "归档编号", "archive_date": "2023-10-01"}]}

def test_archive_details():
    # 发送GET请求获取归档单详情
    response = requests.get(base_url + "/details/归档编号")
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Archive details retrieved", "data": {"archive_number": "归档编号", "archive_date": "2023-10-01"}}

if __name__ == "__main__":
    test_archive_approval()
    test_batch_approval_pass()
    test_batch_approval_reject()
    test_query_archive()
    test_approval_history()
    test_archive_details()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/experiment"

def test_experiment_data_immutability():
    # 定义实验申请单信息
    payload = {
        "实验名称": "实验1",
        "合同名称": "合同A",
        "申请人": "申请人1",
        "申请人手机号": "12345678901",
        "楼号-房号": "1号楼-101",
        "安全员": "安全员1",
        "安全员手机": "12345678901",
        "组长": "组长1",
        "组长手机": "12345678901",
        "反应类型": "类型A",
        "反应温度（℃）": "25",
        "反应压力（MPa）": "1.5",
        "反应介质": "介质A",
        "反应时间起-止": "2023-01-01至2023-01-02",
        "其他反应条件": "条件A",
        "通风橱能否停止": "是",
        "潜在危险": "危险A",
        "应急处置措施": "措施A",
        "危险等级": "等级A"
    }

    # 发送POST请求
    response = requests.post(base_url, json=payload)

    # 验证响应状态码
    assert response.status_code == 200

    # 验证响应体
    assert response.json() == {"message": "Experiment data successfully submitted"}

    # 尝试修改实验数据
    payload["实验名称"] = "实验2"
    response = requests.put(base_url, json=payload)

    # 验证修改失败，状态码应为400
    assert response.status_code == 400

    # 验证响应体
    assert response.json() == {"message": "Experiment data is immutable"}

if __name__ == "__main__":
    test_experiment_data_immutability()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/api"

def test_add_user():
    # 定义新增用户的信息
    payload = {
        "user_account": "test_user_1",
        "user_name": "Test User",
        "avatar": "http://example.com/avatar.png",
        "gender": "male",
        "phone_number": "1234567890",
        "status": "normal"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/users", json=payload)
    # 验证响应状态码
    assert response.status_code == 201
    # 验证响应体
    assert response.json()["message"] == "User added successfully"

def test_edit_user():
    # 定义编辑用户的信息
    payload = {
        "user_name": "Updated User",
        "avatar": "http://example.com/updated_avatar.png",
        "gender": "female",
        "phone_number": "0987654321",
        "status": "normal"
    }
    # 发送PUT请求
    response = requests.put(f"{base_url}/users/test_user_1", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["message"] == "User updated successfully"

def test_get_user_details():
    # 发送GET请求
    response = requests.get(f"{base_url}/users/test_user_1")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["user_account"] == "test_user_1"

def test_freeze_user():
    # 发送PUT请求
    response = requests.put(f"{base_url}/users/test_user_1/freeze")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["message"] == "User frozen successfully"

def test_unfreeze_user():
    # 发送PUT请求
    response = requests.put(f"{base_url}/users/test_user_1/unfreeze")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["message"] == "User unfrozen successfully"

def test_reset_password():
    # 定义重置密码的信息
    payload = {
        "new_password": "new_password123"
    }
    # 发送PUT请求
    response = requests.put(f"{base_url}/users/test_user_1/reset_password", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["message"] == "Password reset successfully"

def test_delete_user():
    # 发送DELETE请求
    response = requests.delete(f"{base_url}/users/test_user_1")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json()["message"] == "User deleted successfully"

def test_query_users():
    # 定义查询条件
    params = {
        "user_account": "test_user",
        "gender": "male",
        "user_name": "Test",
        "phone_number": "1234567890",
        "status": "normal"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/users", params=params)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert len(response.json()) > 0

if __name__ == "__main__":
    test_add_user()
    test_edit_user()
    test_get_user_details()
    test_freeze_user()
    test_unfreeze_user()
    test_reset_password()
    test_delete_user()
    test_query_users()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_create_user():
    # 定义有效的用户信息
    payload = {
        "用户姓名": "张三",
        "头像": "avatar.png",  # 假设文件路径
        "登录密码": "Password123!",
        "确认密码": "Password123!",
        "手机号码": "13800138000",
        "角色分配": "合同管理员",
        "工号": "123456789012345",
        "邮箱": "test@example.com",
        "生日": "1990-01-01",
        "性别": "男"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/create_user", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "User created successfully"}

def test_upload_avatar():
    # 定义有效的头像文件路径
    files = {'头像': open('avatar.png', 'rb')}
    # 发送POST请求
    response = requests.post(f"{base_url}/upload_avatar", files=files)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Avatar uploaded successfully"}

def test_invalid_password():
    # 定义无效的密码（长度不足）
    payload = {
        "用户姓名": "李四",
        "登录密码": "Pass1!",
        "确认密码": "Pass1!",
        "手机号码": "13800138001",
        "角色分配": "销售主管",
        "工号": "123456789012346",
        "邮箱": "test2@example.com",
        "生日": "1990-01-02",
        "性别": "女"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/create_user", json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"message": "Invalid password"}

def test_invalid_phone_number():
    # 定义无效的手机号码（不符合规则）
    payload = {
        "用户姓名": "王五",
        "登录密码": "Password123!",
        "确认密码": "Password123!",
        "手机号码": "23800138000",
        "角色分配": "销售经理",
        "工号": "123456789012347",
        "邮箱": "test3@example.com",
        "生日": "1990-01-03",
        "性别": "男"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/create_user", json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"message": "Invalid phone number"}

def test_invalid_email():
    # 定义无效的邮箱（包含中文）
    payload = {
        "用户姓名": "赵六",
        "登录密码": "Password123!",
        "确认密码": "Password123!",
        "手机号码": "13800138002",
        "角色分配": "库存管理员",
        "工号": "123456789012348",
        "邮箱": "测试@example.com",
        "生日": "1990-01-04",
        "性别": "女"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/create_user", json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"message": "Invalid email"}

def test_role_query():
    # 定义有效的角色名称进行模糊查询
    role_name = "管理员"
    # 发送GET请求
    response = requests.get(f"{base_url}/role_query?role_name={role_name}")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert "合同管理员" in response.json()["roles"]

def test_department_management():
    # 定义有效的部门信息
    payload = {
        "部门名称": "研发部",
        "部门简称": "RD",
        "上级部门": "总公司",
        "手机号": "13800138003",
        "地址": "北京市海淀区",
        "排序": 1,
        "备注": "主要负责产品研发"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/create_department", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Department created successfully"}

if __name__ == "__main__":
    test_create_user()
    test_upload_avatar()
    test_invalid_password()
    test_invalid_phone_number()
    test_invalid_email()
    test_role_query()
    test_department_management()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_create_department():
    # 定义有效的部门名称和简称
    payload = {
        "department_name": "Department1",
        "department_short_name": "Dept1",
        "phone_number": "13800138000",
        "address": "123 Main St",
        "sort_order": 0,
        "remarks": "This is a test department"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/departments", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Department created successfully"}

def test_create_duplicate_department():
    # 定义重复的部门名称和简称
    payload = {
        "department_name": "Department1",
        "department_short_name": "Dept1",
        "phone_number": "13800138000",
        "address": "123 Main St",
        "sort_order": 0,
        "remarks": "This is a test department"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/departments", json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"message": "Department name or short name already exists"}

def test_query_login_logs():
    # 定义查询参数
    params = {
        "log_content": "login",
        "create_time": "2023-10-01"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/logs/login", params=params)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert "logs" in response.json()

def test_query_operation_logs():
    # 定义查询参数
    params = {
        "log_content": "edit",
        "create_time": "2023-10-01",
        "operation_type": "edit"
    }
    # 发送GET请求
    response = requests.get(f"{base_url}/logs/operation", params=params)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert "logs" in response.json()

if __name__ == "__main__":
    test_create_department()
    test_create_duplicate_department()
    test_query_login_logs()
    test_query_operation_logs()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_change_password_different_from_original():
    # 测试新密码与原密码不同的情况
    payload = {
        "username": "user1",
        "old_password": "password1",
        "new_password": "password2"
    }
    response = requests.post(f"{base_url}/change_password", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Password changed successfully"}

def test_change_password_same_as_original():
    # 测试新密码与原密码相同的情况
    payload = {
        "username": "user1",
        "old_password": "password1",
        "new_password": "password1"
    }
    response = requests.post(f"{base_url}/change_password", json=payload)
    assert response.status_code == 400
    assert response.json() == {"message": "New password must be different from the old password"}

def test_confirm_new_password():
    # 测试新密码确认相同的情况
    payload = {
        "username": "user1",
        "old_password": "password1",
        "new_password": "password2",
        "confirm_password": "password2"
    }
    response = requests.post(f"{base_url}/change_password", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Password changed successfully"}

def test_confirm_new_password_mismatch():
    # 测试新密码确认不相同的情况
    payload = {
        "username": "user1",
        "old_password": "password1",
        "new_password": "password2",
        "confirm_password": "password3"
    }
    response = requests.post(f"{base_url}/change_password", json=payload)
    assert response.status_code == 400
    assert response.json() == {"message": "New password and confirmation do not match"}

def test_user_not_found():
    # 测试用户不存在的情况
    payload = {
        "username": "nonexistent_user",
        "password": "password1"
    }
    response = requests.post(f"{base_url}/login", json=payload)
    assert response.status_code == 404
    assert response.json() == {"message": "User not found"}

def test_required_fields_marked():
    # 测试新增、编辑页面中的必填项应给出 * 标识
    response = requests.get(f"{base_url}/create_user")
    assert response.status_code == 200
    assert "*" in response.text  # 假设页面内容包含必填项的 * 标识

def test_required_fields_missing():
    # 测试未输入必填项的情况
    payload = {
        "username": "",
        "password": "password1"
    }
    response = requests.post(f"{base_url}/create_user", json=payload)
    assert response.status_code == 400
    assert response.json() == {"message": "Required fields are missing"}

def test_admin_role_immutability():
    # 测试系统管理员角色不可更改、删除和禁用
    payload = {
        "username": "admin",
        "action": "delete"
    }
    response = requests.post(f"{base_url}/admin_action", json=payload)
    assert response.status_code == 403
    assert response.json() == {"message": "Admin role is immutable"}

if __name__ == "__main__":
    test_change_password_different_from_original()
    test_change_password_same_as_original()
    test_confirm_new_password()
    test_confirm_new_password_mismatch()
    test_user_not_found()
    test_required_fields_marked()
    test_required_fields_missing()
    test_admin_role_immutability()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_sales_contract_management():
    # 测试销售合同管理功能
    endpoint = "/sales_contract_management"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    response = requests.get(base_url + endpoint, headers=headers)
    assert response.status_code == 200
    assert "sales_contracts" in response.json()

def test_sales_contract_approval():
    # 测试销售合同审批功能
    endpoint = "/sales_contract_approval"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    payload = {"contract_id": "123", "status": "approved"}
    response = requests.post(base_url + endpoint, headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Contract approved"

def test_contract_invoice():
    # 测试合同发票功能
    endpoint = "/contract_invoice"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    payload = {"contract_id": "123"}
    response = requests.get(base_url + endpoint, headers=headers, params=payload)
    assert response.status_code == 200
    assert "invoice" in response.json()

def test_contract_actual_receipt():
    # 测试合同实际收款功能
    endpoint = "/contract_actual_receipt"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    payload = {"contract_id": "123", "amount": 1000}
    response = requests.post(base_url + endpoint, headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Receipt recorded"

def test_actual_shipment_info():
    # 测试实际出货信息功能
    endpoint = "/actual_shipment_info"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    payload = {"contract_id": "123"}
    response = requests.get(base_url + endpoint, headers=headers, params=payload)
    assert response.status_code == 200
    assert "shipment_info" in response.json()

def test_pre_contract_experiment_record():
    # 测试合同前实验记录功能
    endpoint = "/pre_contract_experiment_record"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    payload = {"contract_id": "123"}
    response = requests.get(base_url + endpoint, headers=headers, params=payload)
    assert response.status_code == 200
    assert "experiment_records" in response.json()

def test_customer_management():
    # 测试客户管理功能
    endpoint = "/customer_management"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    response = requests.get(base_url + endpoint, headers=headers)
    assert response.status_code == 200
    assert "customers" in response.json()

def test_purchase_contract_management():
    # 测试采购合同管理功能
    endpoint = "/purchase_contract_management"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    response = requests.get(base_url + endpoint, headers=headers)
    assert response.status_code == 200
    assert "purchase_contracts" in response.json()

def test_purchase_contract_approval():
    # 测试采购合同审批功能
    endpoint = "/purchase_contract_approval"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    payload = {"contract_id": "123", "status": "approved"}
    response = requests.post(base_url + endpoint, headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Contract approved"

def test_inbound_order_management():
    # 测试入库单管理功能
    endpoint = "/inbound_order_management"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    response = requests.get(base_url + endpoint, headers=headers)
    assert response.status_code == 200
    assert "inbound_orders" in response.json()

def test_outbound_order_management():
    # 测试出库单管理功能
    endpoint = "/outbound_order_management"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    response = requests.get(base_url + endpoint, headers=headers)
    assert response.status_code == 200
    assert "outbound_orders" in response.json()

def test_supplier_management():
    # 测试供应商管理功能
    endpoint = "/supplier_management"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    response = requests.get(base_url + endpoint, headers=headers)
    assert response.status_code == 200
    assert "suppliers" in response.json()

def test_material_management():
    # 测试材料管理功能
    endpoint = "/material_management"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    response = requests.get(base_url + endpoint, headers=headers)
    assert response.status_code == 200
    assert "materials" in response.json()

def test_inventory_management():
    # 测试库存管理功能
    endpoint = "/inventory_management"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    response = requests.get(base_url + endpoint, headers=headers)
    assert response.status_code == 200
    assert "inventory" in response.json()

def test_inventory_warning():
    # 测试库存预警功能
    endpoint = "/inventory_warning"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    response = requests.get(base_url + endpoint, headers=headers)
    assert response.status_code == 200
    assert "warnings" in response.json()

def test_experiment_application():
    # 测试实验申请单功能
    endpoint = "/experiment_application"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    payload = {"experiment_id": "456"}
    response = requests.post(base_url + endpoint, headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Application submitted"

def test_pre_contract_experiment_application():
    # 测试合同前实验申请单功能
    endpoint = "/pre_contract_experiment_application"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    payload = {"experiment_id": "456"}
    response = requests.post(base_url + endpoint, headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Application submitted"

def test_experiment_approval():
    # 测试实验单审批功能
    endpoint = "/experiment_approval"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    payload = {"experiment_id": "456", "status": "approved"}
    response = requests.post(base_url + endpoint, headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Experiment approved"

def test_pre_contract_experiment_approval():
    # 测试合同前实验单审批功能
    endpoint = "/pre_contract_experiment_approval"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    payload = {"experiment_id": "456", "status": "approved"}
    response = requests.post(base_url + endpoint, headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Experiment approved"

def test_experiment_archiving():
    # 测试实验单归档功能
    endpoint = "/experiment_archiving"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    payload = {"experiment_id": "456"}
    response = requests.post(base_url + endpoint, headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Experiment archived"

def test_experiment_archiving_approval():
    # 测试实验单归档审批功能
    endpoint = "/experiment_archiving_approval"
    headers = {"Authorization": "Bearer <token>"}  # 假设需要认证
    payload = {"experiment_id": "456", "status": "approved"}
    response = requests.post(base_url + endpoint, headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Archiving approved"

if __name__ == "__main__":
    test_sales_contract_management()
    test_sales_contract_approval()
    test_contract_invoice()
    test_contract_actual_receipt()
    test_actual_shipment_info()
    test_pre_contract_experiment_record()
    test_customer_management()
    test_purchase_contract_management()
    test_purchase_contract_approval()
    test_inbound_order_management()
    test_outbound_order_management()
    test_supplier_management()
    test_material_management()
    test_inventory_management()
    test_inventory_warning()
    test_experiment_application()
    test_pre_contract_experiment_application()
    test_experiment_approval()
    test_pre_contract_experiment_approval()
    test_experiment_archiving()
    test_experiment_archiving_approval()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/contract"

def test_create_contract():
    # 定义合同信息
    payload = {
        "合同编号": "HT-202405176119",
        "合同日期": "2024-05-17",
        "合同名称": "测试合同",
        "合同金额": 10000.00,
        "付款方式": "分期付款",
        "客户名称": "客户A",
        "归属部门": "销售部",
        "联系人": "张三",
        "联系方式": "13800138000",
        "备注": "测试备注",
        "评审表编号": "PR-20240517",
        "附件": "test.pdf"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract created successfully"}

def test_create_contract_missing_required_fields():
    # 定义缺少必填字段的合同信息
    payload = {
        "合同编号": "HT-202405176120",
        "合同日期": "2024-05-17",
        "合同名称": "测试合同",
        "合同金额": 10000.00,
        "付款方式": "分期付款",
        "客户名称": "客户A",
        "归属部门": "销售部",
        "联系人": "张三",
        "联系方式": "13800138000"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"message": "Missing required fields"}

def test_create_contract_invalid_amount():
    # 定义合同金额为负数的合同信息
    payload = {
        "合同编号": "HT-202405176121",
        "合同日期": "2024-05-17",
        "合同名称": "测试合同",
        "合同金额": -10000.00,
        "付款方式": "分期付款",
        "客户名称": "客户A",
        "归属部门": "销售部",
        "联系人": "张三",
        "联系方式": "13800138000",
        "备注": "测试备注",
        "评审表编号": "PR-20240517",
        "附件": "test.pdf"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"message": "Invalid contract amount"}

def test_create_contract_invalid_attachment_format():
    # 定义附件格式不正确的合同信息
    payload = {
        "合同编号": "HT-202405176122",
        "合同日期": "2024-05-17",
        "合同名称": "测试合同",
        "合同金额": 10000.00,
        "付款方式": "分期付款",
        "客户名称": "客户A",
        "归属部门": "销售部",
        "联系人": "张三",
        "联系方式": "13800138000",
        "备注": "测试备注",
        "评审表编号": "PR-20240517",
        "附件": "test.txt"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"message": "Invalid attachment format"}

if __name__ == "__main__":
    test_create_contract()
    test_create_contract_missing_required_fields()
    test_create_contract_invalid_amount()
    test_create_contract_invalid_attachment_format()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/contract"

def test_valid_contract_creation():
    # 定义有效的合同信息
    payload = {
        "contract_name": "Sample Contract",
        "contract_number": "CONTRACT-001",
        "contract_status": "Active",
        "contract_date": "2023-10-01",
        "department": "Sales",
        "client_name": "Client A",
        "contract_amount": 100000.00,
        "contact_person": "John Doe",
        "contact_number": "1234567890",
        "review_number": "REVIEW-001",
        "payment_conditions": "Net 30",
        "payment_percentage": 50.00,
        "payment_amount": 50000.00,
        "first_payment_date": "2023-10-15",
        "final_payment_date": "2023-11-15"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract created successfully"}

def test_invalid_payment_percentage():
    # 定义无效的付款比例
    payload = {
        "contract_name": "Sample Contract",
        "contract_number": "CONTRACT-001",
        "contract_status": "Active",
        "contract_date": "2023-10-01",
        "department": "Sales",
        "client_name": "Client A",
        "contract_amount": 100000.00,
        "contact_person": "John Doe",
        "contact_number": "1234567890",
        "review_number": "REVIEW-001",
        "payment_conditions": "Net 30",
        "payment_percentage": 101.00,  # 无效的付款比例
        "payment_amount": 50000.00,
        "first_payment_date": "2023-10-15",
        "final_payment_date": "2023-11-15"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Invalid payment percentage"}

def test_final_payment_before_first_payment():
    # 定义尾款日期早于首款日期的无效合同信息
    payload = {
        "contract_name": "Sample Contract",
        "contract_number": "CONTRACT-001",
        "contract_status": "Active",
        "contract_date": "2023-10-01",
        "department": "Sales",
        "client_name": "Client A",
        "contract_amount": 100000.00,
        "contact_person": "John Doe",
        "contact_number": "1234567890",
        "review_number": "REVIEW-001",
        "payment_conditions": "Net 30",
        "payment_percentage": 50.00,
        "payment_amount": 50000.00,
        "first_payment_date": "2023-11-15",
        "final_payment_date": "2023-10-15"  # 尾款日期早于首款日期
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Final payment date cannot be before first payment date"}

if __name__ == "__main__":
    test_valid_contract_creation()
    test_invalid_payment_percentage()
    test_final_payment_before_first_payment()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/api"

def test_material_info():
    # 测试材料信息接口
    response = requests.get(f"{base_url}/material")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体中的材料信息是否自动带出且不可修改
    data = response.json()
    assert "材料编号" in data and "材料名称" in data and "单价" in data and "数量" in data and "计量单位" in data and "是否免检" in data
    assert data["材料编号"] != "" and data["材料名称"] != "" and data["单价"] != "" and data["数量"] != "" and data["计量单位"] != "" and data["是否免检"] != ""

def test_payment_info():
    # 测试付款信息接口
    response = requests.get(f"{base_url}/payment")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体中的付款信息是否自动带出且不可修改
    data = response.json()
    assert "付款类型" in data and "付款日期" in data and "付款条件" in data and "付款金额" in data and "付款比例" in data
    assert data["付款类型"] != "" and data["付款日期"] != "" and data["付款条件"] != "" and data["付款金额"] != "" and data["付款比例"] != ""

def test_invoice_info():
    # 测试发票信息接口
    response = requests.get(f"{base_url}/invoice")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体中的发票信息是否自动带出且不可修改
    data = response.json()
    assert "发票编号" in data and "发票日期" in data and "开票金额" in data and "计票人员" in data
    assert data["发票编号"] != "" and data["发票日期"] != "" and data["开票金额"] != "" and data["计票人员"] != ""

def test_receipt_info():
    # 测试收款信息接口
    response = requests.get(f"{base_url}/receipt")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体中的收款信息是否自动带出且不可修改
    data = response.json()
    assert "收款编号" in data and "收款日期" in data and "收款方式" in data and "收款金额" in data and "收款人" in data
    assert data["收款编号"] != "" and data["收款日期"] != "" and data["收款方式"] != "" and data["收款金额"] != "" and data["收款人"] != ""

def test_invoice_creation():
    # 测试发票创建接口
    payload = {
        "发票编号": "FP-202405177957",
        "发票日期": "2024-05-17",
        "合同名称": "审批通过",
        "归属部门": "销售部",
        "客户名称": "客户A",
        "开票金额": "一次性"
    }
    response = requests.post(f"{base_url}/create_invoice", json=payload)
    # 验证响应状态码
    assert response.status_code == 201
    # 验证响应体中的发票信息是否正确
    data = response.json()
    assert data["发票编号"] == "FP-202405177957" and data["发票日期"] == "2024-05-17" and data["合同名称"] == "审批通过" and data["归属部门"] == "销售部" and data["客户名称"] == "客户A" and data["开票金额"] == "一次性"

if __name__ == "__main__":
    test_material_info()
    test_payment_info()
    test_invoice_info()
    test_receipt_info()
    test_invoice_creation()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/payment"

def test_upload_single_attachment():
    # 定义有效的附件数据
    files = {'file': open('test_attachment.pdf', 'rb')}
    # 发送POST请求
    response = requests.post(f"{base_url}/upload", files=files)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Attachment uploaded successfully"}

def test_upload_invalid_file_format():
    # 定义无效的附件数据（不支持的格式）
    files = {'file': open('test_attachment.txt', 'rb')}
    # 发送POST请求
    response = requests.post(f"{base_url}/upload", files=files)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Invalid file format"}

def test_upload_large_file():
    # 定义过大的附件数据（超过5MB）
    files = {'file': open('large_attachment.pdf', 'rb')}
    # 发送POST请求
    response = requests.post(f"{base_url}/upload", files=files)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "File size exceeds limit"}

def test_payment_type_validation():
    # 定义分期付款的销售合同数据
    payload = {
        "payment_type": "installment",
        "payment_amount": "1000.00",
        "payment_method": "bank_transfer"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Payment processed successfully"}

def test_invalid_payment_type():
    # 定义无效的付款类型数据
    payload = {
        "payment_type": "invalid_type",
        "payment_amount": "1000.00",
        "payment_method": "bank_transfer"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Invalid payment type"}

if __name__ == "__main__":
    test_upload_single_attachment()
    test_upload_invalid_file_format()
    test_upload_large_file()
    test_payment_type_validation()
    test_invalid_payment_type()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/contract"

def test_contract_creation():
    # 定义合同创建的有效数据
    payload = {
        "合同编号": "HT-202405178532",
        "合同日期": "2024-05-17",
        "合同名称": "测试合同",
        "合同金额": 100000.00
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract created successfully"}

def test_contract_creation_missing_required_fields():
    # 定义合同创建的无效数据，缺少必填项
    payload = {
        "合同编号": "HT-202405178532",
        "合同日期": "2024-05-17"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Missing required fields"}

def test_contract_creation_invalid_amount():
    # 定义合同创建的无效数据，合同金额小于0
    payload = {
        "合同编号": "HT-202405178532",
        "合同日期": "2024-05-17",
        "合同名称": "测试合同",
        "合同金额": -100.00
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Invalid contract amount"}

if __name__ == "__main__":
    test_contract_creation()
    test_contract_creation_missing_required_fields()
    test_contract_creation_invalid_amount()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/contract"

def test_create_contract_with_valid_data():
    # 定义有效的合同数据
    payload = {
        "payment_method": "一次性付款",
        "department": "研发部",
        "customer_name": "客户A",
        "contact_person": "张三",
        "contact_number": "13800138000",
        "review_form_number": "RF-20240517-001",
        "note": "合同备注",
        "attachment": "合同附件.pdf",
        "material_number": "MAT-20240517-001",
        "material_name": "实验材料A",
        "unit_price": "100.00",
        "quantity": "10",
        "unit": "个",
        "payment_type": "一次性付款",
        "payment_date": "2024-05-17",
        "payment_condition": "全款",
        "payment_percentage": "100",
        "payment_amount": "1000.0000",
        "customer_number": "KH-202405174231",
        "customer_name": "客户A",
        "department": "研发部",
        "contact_person": "张三",
        "contact_number": "13800138000",
        "contact_address": "北京市海淀区"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract created successfully"}

def test_create_contract_with_missing_required_fields():
    # 定义缺少必填字段的合同数据
    payload = {
        "payment_method": "一次性付款",
        "department": "研发部",
        "customer_name": "客户A",
        "contact_person": "张三",
        "contact_number": "13800138000",
        "review_form_number": "RF-20240517-001",
        "note": "合同备注",
        "attachment": "合同附件.pdf",
        "material_number": "MAT-20240517-001",
        "material_name": "实验材料A",
        "unit_price": "100.00",
        "quantity": "10",
        "unit": "个",
        "payment_type": "一次性付款",
        "payment_date": "2024-05-17",
        "payment_condition": "全款",
        "payment_percentage": "100",
        "payment_amount": "1000.0000",
        "customer_number": "KH-202405174231",
        "customer_name": "客户A",
        "department": "研发部",
        "contact_person": "张三",
        "contact_number": "13800138000"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Missing required fields"}

def test_create_contract_with_invalid_contact_number():
    # 定义无效的联系电话的合同数据
    payload = {
        "payment_method": "一次性付款",
        "department": "研发部",
        "customer_name": "客户A",
        "contact_person": "张三",
        "contact_number": "12345678901",
        "review_form_number": "RF-20240517-001",
        "note": "合同备注",
        "attachment": "合同附件.pdf",
        "material_number": "MAT-20240517-001",
        "material_name": "实验材料A",
        "unit_price": "100.00",
        "quantity": "10",
        "unit": "个",
        "payment_type": "一次性付款",
        "payment_date": "2024-05-17",
        "payment_condition": "全款",
        "payment_percentage": "100",
        "payment_amount": "1000.0000",
        "customer_number": "KH-202405174231",
        "customer_name": "客户A",
        "department": "研发部",
        "contact_person": "张三",
        "contact_number": "12345678901",
        "contact_address": "北京市海淀区"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Invalid contact number"}

if __name__ == "__main__":
    test_create_contract_with_valid_data()
    test_create_contract_with_missing_required_fields()
    test_create_contract_with_invalid_contact_number()


import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/order"

def test_create_order():
    # 定义有效的出货订单编号和出货日期
    payload = {
        "order_number": "CHDD-202405176298",
        "shipment_date": "2024-05-17",
        "email": "test@example.com",
        "sales_person": "John Doe",
        "remarks": "This is a test order",
        "delivery_address": "123 Test St"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Order created successfully"}

def test_invalid_email():
    # 定义无效的电子邮箱
    payload = {
        "order_number": "CHDD-202405176298",
        "shipment_date": "2024-05-17",
        "email": "invalid_email",
        "sales_person": "John Doe",
        "remarks": "This is a test order",
        "delivery_address": "123 Test St"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Invalid email format"}

def test_missing_required_fields():
    # 定义缺少必填项的请求体
    payload = {
        "order_number": "CHDD-202405176298",
        "email": "test@example.com",
        "sales_person": "John Doe",
        "remarks": "This is a test order"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Missing required fields"}

if __name__ == "__main__":
    test_create_order()
    test_invalid_email()
    test_missing_required_fields()

import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_contract_info_retrieval():
    # 测试获取合同信息接口
    response = requests.get(f"{base_url}/contract_info")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体中的合同信息是否正确
    contract_info = response.json()
    assert "合同名称" in contract_info
    assert "合同编号" in contract_info
    assert "合同状态" in contract_info
    assert "合同日期" in contract_info
    assert "归属部门" in contract_info
    assert "客户名称" in contract_info
    assert "合同金额（元）" in contract_info
    assert "联系人" in contract_info
    assert "联系方式" in contract_info
    assert "评审表编号" in contract_info

def test_material_info_retrieval():
    # 测试获取实验材料信息接口
    response = requests.get(f"{base_url}/material_info")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体中的实验材料信息是否正确
    material_info = response.json()
    assert "材料编号" in material_info
    assert "材料名称" in material_info
    assert "单价（元）" in material_info
    assert "数量" in material_info
    assert "计量单位" in material_info
    assert "是否免检" in material_info

def test_payment_info_retrieval():
    # 测试获取付款方式信息接口
    response = requests.get(f"{base_url}/payment_info")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体中的付款方式信息是否正确
    payment_info = response.json()
    assert "付款类型" in payment_info
    assert "付款日期" in payment_info
    assert "付款条件" in payment_info
    assert "付款金额（元）" in payment_info
    assert "付款比例（%）" in payment_info

def test_invoice_info_retrieval():
    # 测试获取发票信息接口
    response = requests.get(f"{base_url}/invoice_info")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体中的发票信息是否正确
    invoice_info = response.json()
    assert "发票编号" in invoice_info
    assert "发票日期" in invoice_info
    assert "开票金额（元）" in invoice_info
    assert "计票人员" in invoice_info

def test_receipt_info_retrieval():
    # 测试获取实际收款信息接口
    response = requests.get(f"{base_url}/receipt_info")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体中的实际收款信息是否正确
    receipt_info = response.json()
    assert "收款编号" in receipt_info

if __name__ == "__main__":
    test_contract_info_retrieval()
    test_material_info_retrieval()
    test_payment_info_retrieval()
    test_invoice_info_retrieval()
    test_receipt_info_retrieval()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/contract"

def test_contract_creation():
    # 定义合同信息
    payload = {
        "合同编号": "CGHT-202310010001",
        "合同日期": "2023-10-01",
        "合同名称": "销售合同1",
        "合同金额": 1000000.00,
        "付款方式": "全款",
        "客户名称": "客户A",
        "归属部门": "销售部",
        "联系人": "张三",
        "联系方式": "13800138000",
        "备注": "合同备注信息",
        "评审表编号": "评审表1",
        "附件": "合同附件.pdf"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract created successfully"}

def test_contract_update_failure():
    # 尝试更新合同信息，但由于合同信息自动带入且无法修改，预期会失败
    payload = {
        "合同编号": "CGHT-202310010001",
        "合同日期": "2023-10-02",  # 尝试修改合同日期
        "合同名称": "销售合同2",  # 尝试修改合同名称
        "合同金额": 2000000.00,  # 尝试修改合同金额
        "付款方式": "分期",  # 尝试修改付款方式
        "客户名称": "客户B",  # 尝试修改客户名称
        "归属部门": "市场部",  # 尝试修改归属部门
        "联系人": "李四",  # 尝试修改联系人
        "联系方式": "13900139000",  # 尝试修改联系方式
        "备注": "新备注信息",  # 尝试修改备注
        "评审表编号": "评审表2",  # 尝试修改评审表编号
        "附件": "新附件.pdf"  # 尝试修改附件
    }
    # 发送PUT请求
    response = requests.put(f"{base_url}/CGHT-202310010001", json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"message": "Contract information cannot be modified"}

if __name__ == "__main__":
    test_contract_creation()
    test_contract_update_failure()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_create_contract():
    # 定义合同创建的有效数据
    payload = {
        "contract_name": "Contract1",
        "supplier": "SupplierA",
        "department": "DeptA",
        "contract_amount": 1000.50,
        "contract_date": "2024-05-17"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/contract", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Contract created successfully"}

def test_create_material():
    # 定义材料创建的有效数据
    payload = {
        "material_name": "Material1",
        "unit_price": 50.75,
        "quantity": 10,
        "unit": "kg",
        "is_exempt_from_inspection": "No"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/material", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Material created successfully"}

def test_create_receipt():
    # 定义入库单创建的有效数据
    payload = {
        "receipt_date": "2024-05-17",
        "contract_name": "Contract1",
        "department": "DeptA",
        "inspector": "InspectorA",
        "arrival_location": "LocationA"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/receipt", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Receipt created successfully"}

def test_create_material_receipt():
    # 定义材料入库单创建的有效数据
    payload = {
        "material_name": "Material1",
        "unit_price": 50.75,
        "quantity": 5,
        "unit": "kg",
        "is_exempt_from_inspection": "No"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/material_receipt", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Material receipt created successfully"}

if __name__ == "__main__":
    test_create_contract()
    test_create_material()
    test_create_receipt()
    test_create_material_receipt()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_successful_material_entry():
    # 定义有效的入库材料信息
    payload = {
        "入库数量": 7,
        "计量单位": "枚",
        "是否免检": "否",
        "是否质检": "未完成质检",
        "质检编号": "QCS20240517001"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/material_entry", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Material entry successful"}

def test_successful_material_withdrawal():
    # 定义有效的出库信息
    payload = {
        "出库单编号": "CKD-202405175997",
        "出库日期": "2024-05-17",
        "实验单": "实验单编号",
        "归属部门": "研发部",
        "领料人": "张三",
        "出库类型": "实验",
        "经手人": "李四"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/material_withdrawal", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Material withdrawal successful"}

def test_successful_supplier_entry():
    # 定义有效的供应商信息
    payload = {
        "供应商编号": "GYS-202405172616",
        "供应商名称": "供应商A",
        "归属部门": "采购部",
        "联系人": "王五",
        "联系电话": "13800138000",
        "联系地址": "北京市朝阳区",
        "供应商类别": "原材料供应商",
        "电子邮箱": "supplierA@example.com"
    }
    # 发送POST请求
    response = requests.post(f"{base_url}/supplier_entry", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Supplier entry successful"}

if __name__ == "__main__":
    test_successful_material_entry()
    test_successful_material_withdrawal()
    test_successful_supplier_entry()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000"

def test_material_upload():
    # 定义有效的材料图片文件路径
    file_path = "test_image.jpg"
    # 发送POST请求，上传材料图片
    with open(file_path, 'rb') as file:
        response = requests.post(f"{base_url}/upload", files={'file': file})
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "File uploaded successfully"}

def test_material_creation():
    # 定义有效的材料信息
    payload = {
        "material_number": "PC-202405173910",
        "material_name": "Test Material",
        "unit": "个",
        "purchase_price": 100.50,
        "is_exempt_from_inspection": "免检",
        "material_description": "This is a test material",
        "remarks": "Test remarks"
    }
    # 发送POST请求，创建材料
    response = requests.post(f"{base_url}/materials", json=payload)
    # 验证响应状态码
    assert response.status_code == 201
    # 验证响应体
    assert response.json() == {"message": "Material created successfully"}

def test_supplier_upload():
    # 定义有效的供应商资质文件路径
    file_path = "test_document.pdf"
    # 发送POST请求，上传供应商资质
    with open(file_path, 'rb') as file:
        response = requests.post(f"{base_url}/supplier/upload", files={'file': file})
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Supplier document uploaded successfully"}

def test_inventory_operation():
    # 定义有效的库存操作信息
    payload = {
        "operator": "Test Operator",
        "operation_type": "材料入库增加",
        "material_name": "Test Material",
        "quantity": 10,
        "detail_description": "材料进行入库操作！"
    }
    # 发送POST请求，执行库存操作
    response = requests.post(f"{base_url}/inventory/operation", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Inventory operation successful"}

if __name__ == "__main__":
    test_material_upload()
    test_material_creation()
    test_supplier_upload()
    test_inventory_operation()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/inventory"

def test_inventory_increase():
    # 定义盘库增加的测试数据
    payload = {
        "operation_date": "2023-10-01 12:00:00",
        "type": "盘库增加",
        "material_name": "材料A",
        "quantity": 10,
        "detail_description": "材料进行盘赢操作"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Inventory increase successful"}

def test_inventory_decrease():
    # 定义盘库减少的测试数据
    payload = {
        "operation_date": "2023-10-01 12:00:00",
        "type": "盘库减少",
        "material_name": "材料A",
        "quantity": 5,
        "detail_description": "材料进行盘亏操作"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Inventory decrease successful"}

def test_inventory_alert():
    # 定义库存预警的测试数据
    payload = {
        "material_number": "MAT12345",
        "material_name": "材料A",
        "quantity": 100,
        "minimum_safety_stock": 50,
        "maximum_safety_stock": 200
    }
    # 发送POST请求
    response = requests.post(base_url + "/alert", json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Inventory alert set successfully"}

if __name__ == "__main__":
    test_inventory_increase()
    test_inventory_decrease()
    test_inventory_alert()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/contract"

def test_contract_information_retrieval():
    # 发送GET请求以获取合同信息
    response = requests.get(base_url)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体中的字段
    data = response.json()
    assert "contract_amount" in data
    assert "contract_date" in data
    assert "material_number" in data
    assert "material_name" in data
    assert "unit_price" in data
    assert "quantity" in data
    assert "measurement_unit" in data
    assert "is_exempt_from_inspection" in data
    assert "experiment_name" in data
    assert "contract_name" in data
    assert "applicant" in data
    assert "applicant_phone" in data
    assert "building_room" in data
    assert "safety_officer" in data
    assert "safety_officer_phone" in data
    assert "team_leader" in data
    assert "team_leader_phone" in data
    assert "reaction_type" in data
    assert "reaction_temperature" in data
    assert "reaction_pressure" in data
    assert "reaction_medium" in data
    assert "reaction_start_time" in data

def test_contract_information_modification_failure():
    # 定义无效的修改请求
    payload = {
        "contract_amount": 10000,
        "contract_date": "2023-10-01",
        "material_number": "MAT12345",
        "material_name": "Material X",
        "unit_price": 50.00,
        "quantity": 100,
        "measurement_unit": "kg",
        "is_exempt_from_inspection": "No",
        "experiment_name": "Experiment 1",
        "contract_name": "Contract A",
        "applicant": "John Doe",
        "applicant_phone": "12345678901",
        "building_room": "1-1",
        "safety_officer": "Jane Smith",
        "safety_officer_phone": "09876543210",
        "team_leader": "Alice Johnson",
        "team_leader_phone": "11223344556",
        "reaction_type": ["chlorination", "nitration"],
        "reaction_temperature": 80,
        "reaction_pressure": 0.3,
        "reaction_medium": "Water",
        "reaction_start_time": "2023-10-01T10:00:00"
    }
    
    # 发送PUT请求以尝试修改合同信息
    response = requests.put(base_url, json=payload)
    
    # 验证响应状态码为400，表示修改失败
    assert response.status_code == 400
    
    # 验证响应体中的错误信息
    assert response.json() == {"message": "Contract information cannot be modified"}

if __name__ == "__main__":
    test_contract_information_retrieval()
    test_contract_information_modification_failure()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/api"

def test_required_fields():
    # 测试必填项是否正确处理
    payload = {
        "其他反应条件": "测试条件",
        "通风橱能否停止": "是",
        "潜在危险": ["燃烧", "爆炸"],
        "应急处置措施": ["灭火器", "消防沙"]
    }
    response = requests.post(f"{base_url}/submit", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "提交成功"

def test_date_format():
    # 测试日期格式是否正确处理
    payload = {
        "归档日期": "2023-10-01",
        "其他反应条件": "测试条件",
        "通风橱能否停止": "是",
        "潜在危险": ["燃烧", "爆炸"],
        "应急处置措施": ["灭火器", "消防沙"]
    }
    response = requests.post(f"{base_url}/submit", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "提交成功"

def test_enum_values():
    # 测试枚举值是否正确处理
    payload = {
        "通风橱能否停止": "否",
        "潜在危险": ["中毒", "泄露"],
        "应急处置措施": ["通风", "断电"]
    }
    response = requests.post(f"{base_url}/submit", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "提交成功"

def test_other_field_with_input():
    # 测试'其他'字段是否正确处理
    payload = {
        "潜在危险": ["其他"],
        "其他潜在危险": "特殊危险",
        "应急处置措施": ["其他特殊处理要求"],
        "其他特殊处理要求": "特殊处理"
    }
    response = requests.post(f"{base_url}/submit", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "提交成功"

def test_auto_filled_fields():
    # 测试自动填充字段是否正确处理
    payload = {
        "材料编号": "MAT12345",
        "材料名称": "测试材料",
        "数量": 10,
        "剩余数量": 5,
        "计量单位": "个"
    }
    response = requests.post(f"{base_url}/submit", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "提交成功"

def test_unique_constraints():
    # 测试唯一性约束是否正确处理
    payload = {
        "归档编号": "ARCHIVE123"
    }
    response = requests.post(f"{base_url}/submit", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "提交成功"

if __name__ == "__main__":
    test_required_fields()
    test_date_format()
    test_enum_values()
    test_other_field_with_input()
    test_auto_filled_fields()
    test_unique_constraints()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/experiment"

def test_experiment_data_auto_fill():
    # 定义实验单信息
    payload = {
        "安全员": "安全员1",
        "安全员手机": "12345678901",
        "组长": "组长1",
        "组长手机": "12345678901",
        "反应类型": "类型1",
        "反应温度（℃）": 100,
        "反应压力（MPa）": 1.5,
        "反应介质": "介质1",
        "反应时间起": "2023-01-01",
        "反应时间止": "2023-01-02",
        "其他反应条件": "条件1",
        "通风橱能否停止": "是",
        "潜在危险": "危险1",
        "应急处置措施": "措施1",
        "危险等级": "等级1"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Experiment data auto-filled successfully"}

if __name__ == "__main__":
    test_experiment_data_auto_fill()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/experiment"

def test_experiment_data_auto_fill():
    # 定义测试数据
    payload = {
        "组长手机": "12345678901",
        "实验材料": "材料A",
        "反应类型": "类型A",
        "反应温度（℃）": 25,
        "反应压力（MPa）": 1.5,
        "反应介质": "介质A",
        "反应时间（h）": "2023-10-01T12:00:00Z",
        "其他反应条件": "条件A",
        "通风橱能否停止": "是",
        "潜在危险": "危险A",
        "应急处置措施": "措施A",
        "组长意见": "同意",
        "部门意见": "批准"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    response_data = response.json()
    assert response_data["组长手机"] == "12345678901"
    assert response_data["实验材料"] == "材料A"
    assert response_data["反应类型"] == "类型A"
    assert response_data["反应温度（℃）"] == 25
    assert response_data["反应压力（MPa）"] == 1.5
    assert response_data["反应介质"] == "介质A"
    assert response_data["反应时间（h）"] == "2023-10-01T12:00:00Z"
    assert response_data["其他反应条件"] == "条件A"
    assert response_data["通风橱能否停止"] == "是"
    assert response_data["潜在危险"] == "危险A"
    assert response_data["应急处置措施"] == "措施A"
    assert response_data["组长意见"] == "同意"
    assert response_data["部门意见"] == "批准"

if __name__ == "__main__":
    test_experiment_data_auto_fill()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/experiment"

def test_experiment_details_auto_filled():
    # 定义实验单信息
    payload = {
        "experiment_name": "实验名称",
        "contract_name": "合同名称",
        "applicant": "申请人",
        "applicant_phone": "12345678901",
        "building_room": "楼号-房号",
        "safety_officer": "安全员",
        "safety_officer_phone": "12345678901"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    response_data = response.json()
    assert response_data["experiment_name"] == "实验名称"
    assert response_data["contract_name"] == "合同名称"
    assert response_data["applicant"] == "申请人"
    assert response_data["applicant_phone"] == "12345678901"
    assert response_data["building_room"] == "楼号-房号"
    assert response_data["safety_officer"] == "安全员"
    assert response_data["safety_officer_phone"] == "12345678901"

def test_material_details_auto_filled():
    # 定义实验材料信息
    payload = {
        "material_id": "材料编号",
        "material_name": "材料名称",
        "unit_price": "123.45",
        "quantity": "1234567",
        "unit": "计量单位",
        "is_exempt_from_inspection": "是否免检"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    response_data = response.json()
    assert response_data["material_id"] == "材料编号"
    assert response_data["material_name"] == "材料名称"
    assert response_data["unit_price"] == "123.45"
    assert response_data["quantity"] == "1234567"
    assert response_data["unit"] == "计量单位"
    assert response_data["is_exempt_from_inspection"] == "是否免检"

def test_safety_details_auto_filled():
    # 定义安全员和组长信息
    payload = {
        "safety_officer": "安全员",
        "safety_officer_phone": "12345678901",
        "team_leader": "组长",
        "team_leader_phone": "12345678901",
        "note": "备注"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    response_data = response.json()
    assert response_data["safety_officer"] == "安全员"
    assert response_data["safety_officer_phone"] == "12345678901"
    assert response_data["team_leader"] == "组长"
    assert response_data["team_leader_phone"] == "12345678901"
    assert response_data["note"] == "备注"

if __name__ == "__main__":
    test_experiment_details_auto_filled()
    test_material_details_auto_filled()
    test_safety_details_auto_filled()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/experiment"

def test_auto_populate_experiment_info():
    # 定义实验单信息
    payload = {
        "实验名称": "实验1",
        "归属部门": "部门A",
        "申请人": "申请人A",
        "申请人手机号": "12345678901",
        "楼号-房号": "1号楼-101",
        "安全员": "安全员A",
        "安全员手机": "12345678901",
        "组长": "组长A",
        "组长手机": "12345678901",
        "反应类型": "类型A",
        "反应温度（℃）": 25,
        "反应压力（MPa）": 1.5,
        "反应介质": "介质A",
        "反应时间起-止": "2023-10-01T00:00:00Z/2023-10-01T01:00:00Z",
        "其他反应条件": "条件A",
        "通风橱能否停止": "能",
        "潜在危险": "危险A",
        "应急处置措施": "措施A",
        "危险等级": "等级A"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Experiment information auto-populated successfully"}

if __name__ == "__main__":
    test_auto_populate_experiment_info()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/experiment"

def test_fetch_experiment_material_info():
    # 测试自动带出实验材料信息接口
    response = requests.get(f"{base_url}/material")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体中的材料信息是否为只读
    material_info = response.json()
    assert all(value['editable'] == False for value in material_info.values())

def test_fetch_experiment_archive_info():
    # 测试自动带入实验归档单信息接口
    response = requests.get(f"{base_url}/archive")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体中的归档信息是否为只读
    archive_info = response.json()
    assert all(value['editable'] == False for value in archive_info.values())

def test_fetch_experiment_info():
    # 测试自动带入实验单信息接口
    response = requests.get(f"{base_url}/info")
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体中的实验信息是否为只读
    experiment_info = response.json()
    assert all(value['editable'] == False for value in experiment_info.values())

if __name__ == "__main__":
    test_fetch_experiment_material_info()
    test_fetch_experiment_archive_info()
    test_fetch_experiment_info()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/experiment"

def test_auto_populate_experiment_info():
    # 定义实验单信息
    payload = {
        "experiment_name": "实验名称",
        "department": "归属部门",
        "applicant": "申请人",
        "applicant_phone": "12345678901",
        "building_room": "楼号-房号",
        "safety_officer": "安全员",
        "safety_officer_phone": "12345678901",
        "team_leader": "组长",
        "team_leader_phone": "12345678901",
        "reaction_type": "反应类型",
        "reaction_temperature": "25",
        "reaction_pressure": "1.5",
        "reaction_medium": "反应介质",
        "reaction_time_start": "2023-10-01",
        "reaction_time_end": "2023-10-02",
        "other_reaction_conditions": "其他反应条件",
        "ventilation_can_stop": "通风橱能否停止",
        "potential_hazard": "潜在危险",
        "emergency_measures": "应急处置措施",
        "hazard_level": "危险等级"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Experiment information auto-populated successfully"}

def test_auto_populate_material_info():
    # 定义实验材料信息
    payload = {
        "material_number": "材料编号",
        "material_name": "材料名称",
        "unit_price": "12345.67",
        "quantity": "1234567",
        "unit": "计量单位",
        "is_exempt_from_inspection": "是否免检"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "Material information auto-populated successfully"}

def test_user_account_creation():
    # 定义用户账号信息
    payload = {
        "user_account": "user_account_123",
        "user_name": "用户姓名",
        "avatar": "avatar.jpg"
    }
    
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    
    # 验证响应状态码
    assert response.status_code == 200
    
    # 验证响应体
    assert response.json() == {"message": "User account created successfully"}

if __name__ == "__main__":
    test_auto_populate_experiment_info()
    test_auto_populate_material_info()
    test_user_account_creation()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/register"

def test_valid_registration():
    # 定义有效的注册信息
    payload = {
        "username": "user1",
        "password": "Password1!",
        "confirm_password": "Password1!",
        "phone_number": "13800138000",
        "role_assignment": "合同管理员",
        "employee_id": "123456789012345",
        "email": "user1@example.com",
        "birthday": "1990-01-01",
        "gender": "男"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Registration successful"}

def test_invalid_password_length():
    # 定义密码长度不符合要求的注册信息
    payload = {
        "username": "user1",
        "password": "Pass1!",
        "confirm_password": "Pass1!",
        "phone_number": "13800138000",
        "role_assignment": "合同管理员",
        "employee_id": "123456789012345",
        "email": "user1@example.com",
        "birthday": "1990-01-01",
        "gender": "男"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Password must be between 8 and 18 characters"}

def test_invalid_phone_number():
    # 定义手机号不符合要求的注册信息
    payload = {
        "username": "user1",
        "password": "Password1!",
        "confirm_password": "Password1!",
        "phone_number": "23800138000",
        "role_assignment": "合同管理员",
        "employee_id": "123456789012345",
        "email": "user1@example.com",
        "birthday": "1990-01-01",
        "gender": "男"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Invalid phone number"}

def test_invalid_email():
    # 定义邮箱不符合要求的注册信息
    payload = {
        "username": "user1",
        "password": "Password1!",
        "confirm_password": "Password1!",
        "phone_number": "13800138000",
        "role_assignment": "合同管理员",
        "employee_id": "123456789012345",
        "email": "user1example.com",
        "birthday": "1990-01-01",
        "gender": "男"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Invalid email format"}

if __name__ == "__main__":
    test_valid_registration()
    test_invalid_password_length()
    test_invalid_phone_number()
    test_invalid_email()
    
import requests
import json

# 定义接口的基本URL
base_url = "http://localhost:5000/log"

def test_log_creation():
    # 定义日志创建的请求体
    payload = {
        "耗时（毫秒）": 5,
        "日志类型": "操作日志",
        "操作类型": "新增",
        "创建时间": "2023-10-01 12:00:00"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Log created successfully"}

def test_log_creation_with_different_operation_type():
    # 定义日志创建的请求体，操作类型为编辑
    payload = {
        "耗时（毫秒）": 5,
        "日志类型": "操作日志",
        "操作类型": "编辑",
        "创建时间": "2023-10-01 12:00:00"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 200
    # 验证响应体
    assert response.json() == {"message": "Log created successfully"}

def test_log_creation_with_invalid_operation_type():
    # 定义日志创建的请求体，操作类型为无效值
    payload = {
        "耗时（毫秒）": 5,
        "日志类型": "操作日志",
        "操作类型": "无效操作",
        "创建时间": "2023-10-01 12:00:00"
    }
    # 发送POST请求
    response = requests.post(base_url, json=payload)
    # 验证响应状态码
    assert response.status_code == 400
    # 验证响应体
    assert response.json() == {"error": "Invalid operation type"}

if __name__ == "__main__":
    test_log_creation()
    test_log_creation_with_different_operation_type()
    test_log_creation_with_invalid_operation_type()
import requests
import json

BASE_URL = "http://127.0.0.1:5000/login"

# def test_get_method():
#     response = requests.get(BASE_URL)
#     assert response.status_code == 405

# def test_post_method():
#     response = requests.post(BASE_URL, json={})
#     assert response.status_code != 405

# def test_empty_username():
#     response = requests.post(BASE_URL, json={"username": "", "password": "password1"})
#     assert response.status_code == 400
#     assert response.json() == {'message': 'Invalid username format'}

# def test_empty_password():
#     response = requests.post(BASE_URL, json={"username": "user1", "password": ""})
#     assert response.status_code == 400
#     assert response.json() == {'message': 'Invalid password format'}

def test_invalid_username_format():
    response = requests.post(BASE_URL, json={"username": "user!1", "password": "password1"})
    assert response.status_code == 400
    assert response.json() == {'message': 'Invalid username format'}

def test_short_password():
    response = requests.post(BASE_URL, json={"username": "user1", "password": "pass"})
    assert response.status_code == 400
    assert response.json() == {'message': 'Invalid password format'}

def test_long_password():
    response = requests.post(BASE_URL, json={"username": "user1", "password": "thisisaverylongpassword1234567890"})
    assert response.status_code == 400
    assert response.json() == {'message': 'Invalid password format'}

def test_correct_credentials():
    response = requests.post(BASE_URL, json={"username": "user1", "password": "password1"})
    assert response.status_code == 200
    assert response.json() == {'message': 'Login successful'}

def test_incorrect_password():
    response = requests.post(BASE_URL, json={"username": "user1", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.json() == {'message': 'Invalid credentials'}

# def test_nonexistent_user():
#     response = requests.post(BASE_URL, json={"username": "nonexistentuser", "password": "password1"})
#     assert response.status_code == 401
#     assert response.json() == {'message': 'Invalid credentials'}

if __name__ == "__main__":
    # test_get_method()
    # test_post_method()
    # test_empty_username()
    # test_empty_password()
    test_invalid_username_format()
    test_short_password()
    test_long_password()
    test_correct_credentials()
    test_incorrect_password()
    # test_nonexistent_user()
    print("All tests passed!")
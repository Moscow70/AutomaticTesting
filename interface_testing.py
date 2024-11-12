from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# 假设我们有一个用户数据库，这里我们使用一个简单的字典来模拟
users = {
    'user1': 'password1',
    'user2': 'password2'
}

# 定义正则表达式来验证用户名和密码
username_regex = re.compile(r'^[a-zA-Z0-9]+$')
password_regex = re.compile(r'^[a-zA-Z0-9]{8,16}$')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # 验证用户名和密码是否符合要求
    if not username_regex.match(username):
        return jsonify({'message': 'Invalid username format'}), 400
    if not password_regex.match(password):
        return jsonify({'message': 'Invalid password format'}), 400

    if username in users and users[username] == password:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)

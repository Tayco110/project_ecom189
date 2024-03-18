from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de um banco de dados simples
users_db = []

@app.route('/register', methods=['POST'])
def register():
    user_data = request.json
    users_db.append(user_data)
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    credentials = request.json
    user = next((user for user in users_db if user['email'] == credentials['email'] and user['password'] == credentials['password']), None)
    if user:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(port=5001)
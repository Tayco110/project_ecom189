from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de um banco de dados simples
orders_db = []

@app.route('/orders', methods=['POST'])
def create_order():
    order_data = request.json
    orders_db.append(order_data)
    return jsonify({"message": "Order created successfully"}), 201

@app.route('/orders', methods=['GET'])
def list_orders():
    return jsonify(orders_db)

if __name__ == '__main__':
    app.run(port=5003)
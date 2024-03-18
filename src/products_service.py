from flask import Flask, jsonify

app = Flask(__name__)

# Simulação de um banco de dados simples
products_db = [
    {"id": 1, "name": "Smartphone", "price": 300},
    {"id": 2, "name": "Laptop", "price": 800},
]

@app.route('/products', methods=['GET'])
def list_products():
    return jsonify(products_db)

if __name__ == '__main__':
    app.run(port=5002)
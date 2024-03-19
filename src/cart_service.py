import json

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Simulação de um armazenamento de dados em memória
cart_items = []

@app.route('/cart', methods=['GET', 'POST'])
def manage_cart():
    if request.method == 'POST':
        item = request.json
        cart_items.append(item)
        return jsonify({"message": "Item added to cart", "cart": cart_items}), 200
    else:
        # Retornar os itens no carrinho
        return jsonify(cart_items)

@app.route('/cart/remove', methods=['POST'])
def remove_item():
    try:
        global cart_items
        request_data = request.json
        product_id = request_data['product_id']
        for item in cart_items:
            cart_removed = item
            item = eval(item)
            if item['product_id'] == int(product_id):
                cart_items.remove(cart_removed)
                return jsonify({"message": "Item removed from cart", "cart": cart_items}), 200
        return jsonify({"message": "Item not found in cart"}), 404
    except Exception as e:
        print(e)

@app.route('/cart/checkout', methods=['POST'])
def checkout():
    if cart_items:
        cart_items.clear()  # Limpar o carrinho após a compra
        return jsonify({"message": "Checkout successful"}), 200
    else:
        return jsonify({"message": "Cart is empty"}), 400

if __name__ == '__main__':
    app.run(port=5004)
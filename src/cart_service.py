from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de um armazenamento de dados em memória
cart_items = []

@app.route('/cart', methods=['GET', 'POST'])
def manage_cart():
    if request.method == 'POST':
        # Adicionar um item ao carrinho
        item = request.json
        cart_items.append(item)
        return jsonify({"message": "Item added to cart", "cart": cart_items}), 200
    else:
        # Retornar os itens no carrinho
        return jsonify(cart_items)

@app.route('/cart/checkout', methods=['POST'])
def checkout():
    if cart_items:
        cart_items.clear()  # Limpar o carrinho após a compra
        return jsonify({"message": "Checkout successful"}), 200
    else:
        return jsonify({"message": "Cart is empty"}), 400

if __name__ == '__main__':
    app.run(port=5004)
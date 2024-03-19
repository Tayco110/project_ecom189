import json
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessário para usar a sessão

USER_SERVICE_URL = 'http://localhost:5001'
PRODUCT_SERVICE_URL = 'http://localhost:5002'
ORDER_SERVICE_URL = 'http://localhost:5003'
CART_SERVICE_URL = 'http://localhost:5004'

@app.route('/')
def index():
    response = requests.get(f'{PRODUCT_SERVICE_URL}/products')
    products = response.json()
    return render_template('landing.html', products=products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'password': request.form['password']
        }
        response = requests.post(f'{USER_SERVICE_URL}/register', json=user_data)
        if response.status_code == 201:
            return redirect(url_for('login'))
        else:
            return "Erro no registro", 400
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        credentials = {
            'email': request.form['email'],
            'password': request.form['password']
        }
        response = requests.post(f'{USER_SERVICE_URL}/login', json=credentials)
        if response.status_code == 200:
            session['user'] = credentials['email']
            return redirect(url_for('index'))
        else:
            return "Login falhou", 401
    return render_template('login.html')

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        product = request.form['product']
        requests.post(f'{CART_SERVICE_URL}/cart', json=product)
        return redirect(url_for('cart'))
    else:
        response = requests.get(f'{CART_SERVICE_URL}/cart')
        cart_items = [json.loads(item.replace("'", '"')) for item in response.json()]
        return render_template('cart.html', cart_items=cart_items)

@app.route('/cart/remove', methods=['POST'])
def remove_cart():
    remove_data = {
        'product_id': request.form['product_id']
    }
    requests.post(f'{CART_SERVICE_URL}/cart/remove', json=remove_data)
    return redirect(url_for('cart'))
@app.route('/cart/checkout', methods=['POST'])
def checkout():
    requests.post(f'{CART_SERVICE_URL}/cart/checkout')
    return redirect(url_for('index'))

@app.route('/order', methods=['POST'])
def order():
    order_data = {
        'user_id': session.get('user_id', 1),  # exemplo simplificado
        'product_id': request.form['product_id']
    }
    requests.post(f'{ORDER_SERVICE_URL}/orders', json=order_data)
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(port=5000)
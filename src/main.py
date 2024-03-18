from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

USER_SERVICE_URL = 'http://localhost:5001'
PRODUCT_SERVICE_URL = 'http://localhost:5002'
ORDER_SERVICE_URL = 'http://localhost:5003'

@app.route('/')
def index():
    response = requests.get(f'{PRODUCT_SERVICE_URL}/products')
    products = response.json()
    return render_template('index.html', products=products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_data = {
            'email': request.form['email'],
            'password': request.form['password'],
            'name': request.form['name']
        }
        requests.post(f'{USER_SERVICE_URL}/register', json=user_data)
        return redirect(url_for('login'))
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
            return redirect(url_for('index'))
        else:
            return 'Login Failed', 401
    return render_template('login.html')

@app.route('/order', methods=['POST'])
def order():
    order_data = {
        'user_id': 1,  # This should be dynamically set based on logged-in user
        'product_id': request.form['product_id']
    }
    requests.post(f'{ORDER_SERVICE_URL}/orders', json=order_data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000)
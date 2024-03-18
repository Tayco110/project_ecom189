from flask import Flask, jsonify

app = Flask(__name__)

# Simulação de um banco de dados simples
# products_db = [
#     {"id": 1, "name": "Smartphone", "price": 300},
#     {"id": 2, "name": "Laptop", "price": 800},
# ]

products = [
    {
        "product_id" : 1,
        "name": "Smartphone",
        "price": 1500.0,
        "description": "O melhor smartphone do mercado",
        "image_url": "https://www.kadri.com.br/sys/corteimg.asp?img=amp-35411_1.jpg&sys=produtos&cut=1&w1=906&h1=906",
        "category": "smartphones"
    },
    {
        "product_id" : 2,
        "name": "Notebook",
        "price": 3000.0,
        "description": "O notebook mais potente do mercado",
        "image_url": "https://m.media-amazon.com/images/I/51f5MvatbsL._AC_SY450_.jpg",
        "category": "notebooks"
    },
    {
        "product_id" : 3,
        "name": "Tablet",
        "price": 800.0,
        "description": "O tablet mais portátil do mercado",
        "image_url": "https://a-static.mlcdn.com.br/1500x1500/tablet-samsung-galaxy-tab-s6-lite-com-caneta-android-12-4g-104-wi-fi-128gb-octa-core-5mp/magazineluiza/235402700/d90d98a85a5bed45434fd1e1c7cac672.jpg",
        "category": "acessórios"
    },
]

@app.route('/products', methods=['GET'])
def list_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(port=5002)
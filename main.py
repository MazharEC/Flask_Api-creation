from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def test_api():
    return 'Hello, World!'

@app.route('/products', methods=['GET'])
def get_products():
    product = [
        {"id": 1, "name": "Shirt", "price": 1500},
        {"id": 2, "name": "pant", "price": 1500},
        {"id": 3, "name": "shoe", "price": 2500},
        {"id": 4, "name": "jeans", "price": 1500},
    ]
    return product 



if __name__ == '__main__':
    app.run(debug = True)
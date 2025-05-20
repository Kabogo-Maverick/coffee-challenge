from flask import Flask, jsonify
from model.customer import Customer
from model.coffee import Coffee

app = Flask(__name__)

# Setup sample data (like your main.py)
joan = Customer("Joan")
kelly = Customer("Kelly")
omena = Coffee("Omena")

joan.create_order(omena, 4.5)

@app.route('/')
def home():
    return "Welcome to the Coffee Challenge API!"

@app.route('/orders')
def orders():
    orders_list = []
    for order in joan.orders():
        orders_list.append({
            "customer": order.customer.name,
            "coffee": order.coffee.name,
            "price": order.price,
        })
    return jsonify(orders_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

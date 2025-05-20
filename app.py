from flask import Flask, jsonify
from model.customer import Customer
from model.coffee import Coffee
from model.order import Order

app = Flask(__name__)

# Sample data (if not already created elsewhere)
if not Customer.all():  # Prevent duplicates on re-runs
    joan = Customer("Joan")
    kelly = Customer("Kelly")
    rafiki = Customer("Rafiki")
    nimoh = Customer("Nimoh")
    durk = Customer("Durk")

    omena = Coffee("Omena")
    choma = Coffee("Choma")
    ugali = Coffee("Ugali")
    chapati = Coffee("Chapati")

    joan.create_order(omena, 400)
    kelly.create_order(choma, 700)
    rafiki.create_order(ugali, 200)
    nimoh.create_order(choma, 430)
    durk.create_order(chapati, 350)
    joan.create_order(chapati, 375)
    kelly.create_order(omena, 325)
    nimoh.create_order(omena, 375)

@app.route("/")
def home():
    return """
    <h1>☕ Coffee Challenge API</h1>
    <p>Welcome to my Python OOP project where Customers order Coffees!</p>
    <h2>Available Endpoints:</h2>
    <ul>
        <li><a href='/customers'>/customers</a> - View all customers</li>
        <li><a href='/coffees'>/coffees</a> - View all coffees</li>
        <li><a href='/orders'>/orders</a> - View all orders</li>
    </ul>
    <p>See the full project on <a href='https://github.com/Kabogo-Maverick/coffee-challenge' target='_blank'>GitHub</a>.</p>
    """

@app.route("/customers")
def customers():
    return jsonify([customer.name for customer in Customer.all()])

@app.route("/coffees")
def coffees():
    return jsonify([coffee.name for coffee in Coffee.all()])

@app.route("/orders")
def orders():
    return jsonify([
        {
            "customer": order.customer.name,
            "coffee": order.coffee.name,
            "price": f"Ksh. {int(order.price)}"
        } for order in Order.all()
    ])

if __name__ == "__main__":
    app.run(debug=True)

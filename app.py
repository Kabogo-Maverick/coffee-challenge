from flask import Flask, jsonify
from model.customer import Customer
from model.coffee import Coffee

app = Flask(__name__)

# === Sample Data Setup ===
joan = Customer("Joan")
kelly = Customer("Kelly")
rafiki = Customer("Rafiki")
nimoh = Customer("Nimoh")
durk = Customer("Durk")

omena = Coffee("Omena")
choma = Coffee("Choma")
ugali = Coffee("Ugali")
chapati = Coffee("Chapati")

# Create orders
joan.create_order(omena, 450.0)
kelly.create_order(choma, 500.0)
rafiki.create_order(ugali, 275.0)
nimoh.create_order(choma, 450.0)
durk.create_order(chapati, 325.0)
joan.create_order(chapati, 375.0)
kelly.create_order(omena, 325.0)
nimoh.create_order(omena, 375.0)

all_customers = [joan, kelly, rafiki, nimoh, durk]
all_coffees = [omena, choma, ugali, chapati]

# === Routes ===

@app.route('/')
def home():
    return """
    <h1>Welcome to the Coffee Challenge API!</h1>
    <p>Explore these endpoints:</p>
    <ul>
        <li><a href="/orders">/orders</a> - View all orders</li>
        <li><a href="/customers">/customers</a> - View all customers</li>
        <li><a href="/coffees">/coffees</a> - View all coffee items with stats</li>
    </ul>
    """

@app.route('/orders')
def orders():
    orders_list = []
    for customer in all_customers:
        for order in customer.orders():
            orders_list.append({
                "customer": order.customer.name,
                "coffee": order.coffee.name,
                "price (Ksh)": f"Ksh.{order.price:.2f}"  # Format price directly
            })
    return jsonify(orders_list)

@app.route('/customers')
def customers():
    return jsonify([customer.name for customer in all_customers])

@app.route('/coffees')
def coffees():
    coffee_data = []
    for coffee in all_coffees:
        coffee_data.append({
            "coffee": coffee.name,
            "total_orders": coffee.num_orders(),
            "average_price (Ksh)": f"Ksh.{coffee.average_price():.2f}",  # No multiplication
            "customers": [cust.name for cust in coffee.customers()]
        })
    return jsonify(coffee_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# To run the Flask app, use the command:    
# python app.py
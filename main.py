from model.customer import Customer
from model.coffee import Coffee

def main():
    # Create Customers
    joan = Customer("Joan")
    kelly = Customer("Kelly")
    rafiki = Customer("Rafiki")
    nimoh = Customer("Nimoh")
    durk = Customer("Durk")

    # Create Coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    americano = Coffee("Americano")
    cappuccino = Coffee("Cappuccino")

    # Customers place orders
    joan.create_order(latte, 450)
    kelly.create_order(espresso, 375)
    rafiki.create_order(americano, 300)
    nimoh.create_order(cappuccino, 500)
    durk.create_order(latte, 425)
    joan.create_order(cappuccino, 475)
    kelly.create_order(latte, 400)

    # Print each customer's orders
    for customer in [joan, kelly, rafiki, nimoh, durk]:
        print(f"{customer.name}'s Orders:")
        for order in customer.orders():
            print(f" - {order.coffee.name}: Ksh.{order.price}")
        print()

    # Print stats for each coffee
    for coffee in [latte, espresso, americano, cappuccino]:
        print(f"{coffee.name} Stats:")
        print(f" - Total orders: {coffee.num_orders()}")
        print(f" - Average price: Ksh.{coffee.average_price():.2f}")
        customers = coffee.customers()
        if customers:
            print(" - Customers who ordered:")
            for cust in customers:
                print(f"    * {cust.name}")
        else:
            print(" - No customers yet.")
        print()

if __name__ == "__main__":
    main()

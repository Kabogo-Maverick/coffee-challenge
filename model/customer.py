class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string with 1 to 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

   
    def create_order(self, coffee, price):
        from model.order import Order  # <-- add 'model.' to fix import
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order




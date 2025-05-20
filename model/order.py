from model.customer import Customer
from model.coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of the Customer class.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of the Coffee class.")
        if not isinstance(price, (float, int)):
            raise TypeError("price must be a float or an int.")
        if not 1.0 <= price <= 10000.0:  # Updated range to support Ksh pricing
            raise ValueError("price must be between 1.0 and 10000.0 (inclusive).")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

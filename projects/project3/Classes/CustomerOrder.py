# File: CustomerOrder.py

# Imports
from datastructures.array import Array
from Drink import Drink

# Implemetation

class CustomerOrder():
    def __init__(self, name):
        """Constructor function for the CustomerOrder class.
        Args:
            name (str): The name of the customer
        Returns:
            None
        Raises:
            TypeError:
                name must be a string
        """
        # errors
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        # instance variables
        self.name: str = name
        self.order: Array[Drink] = Array(type=Drink)

    # methods
    def add(self, order):
        for item in order:
            if not isinstance(item, Drink):
                raise TypeError("Item must be a string")
            self.order.append(item)
    
    # properties
    @property
    def name(self):
        return self.name
    @property
    def order(self):
        return self.order
# File: CustomerOrder.py

# Imports
from datastructures.array import Array
from projects.project3.Drink import Drink

# Implementation

class CustomerOrder():
    def __init__(self, cust_name):
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
        if not isinstance(cust_name, str):
            raise TypeError("Name must be a string")
        # instance variables
        self.cust_name: str = cust_name
        self.order: Array[Drink] = Array(data_type=Drink)

    # methods
    def add(self, order:Drink):
        """Method to add items to the order. Appends each item in order to the order list
        Args:
            order (list): A list of Drink items to add
        Returns:
            None
        Raises:
            TypeError:
                order must be a list
                each item in order must be a Drink
        """
        # errors

        if not isinstance(order, Drink):
            raise TypeError("Order must be a string")
        self.order.append(order)

    def get_total_price(self) -> float:
        total = 0
        for drink in self.order:
            total += drink.price
        return total

    def __str__(self) -> str:
        return f"{self.cust_name}: {self.order}"
    
    # properties
    def name(self) -> str:
        return self.cust_name
    def order(self) -> list:
        return self.order
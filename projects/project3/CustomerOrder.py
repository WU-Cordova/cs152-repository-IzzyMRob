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
                cust_name must be a string
        """
        # errors
        if not isinstance(cust_name, str):
            raise TypeError("Name must be a string")
        # instance variables
        self.cust_name: str = cust_name
        self.order: Array[Drink] = Array(data_type=Drink)

    # methods
    def add(self, order:Drink):
        """Method to add items to the order. Appends the item to the order list.
        Args:
            order (list): A Drink item to add
        Returns:
            None
        Raises:
            TypeError:
                order must be a Drink
        """
        # errors
        if not isinstance(order, Drink):
            raise TypeError("Order must be a string")
        # add Drink to order variable
        self.order.append(order)

    def get_total_price(self) -> float:
        """Method to calculate and return the total price of the order"""
        total = 0
        for drink in self.order:
            total += drink.price
        return total

    def __str__(self) -> str:
        """Returns a string representation of the CustomerOrder"""
        return f"{self.cust_name}: {self.order}"
    
    # properties
    def name(self) -> str:
        """Returns the name of the customer making the order"""
        return self.cust_name
    def order(self) -> list:
        """Returns the list of all drinks added to the order"""
        return self.order
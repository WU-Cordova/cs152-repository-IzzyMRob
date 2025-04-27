# File: Drink.py

# Imports
from projects.project3.text import price_key

# Implementation

class Drink():
    def __init__(self, name:str, size:str='Medium', custom:str=None):
        """Constructor function for the Drink class.
        Args:
            name (str): The name of the drink
            size (str): The size of the drink, eg. S, M, L
            custom (str): Customizations entered by the customer
        Returns:
            None
        Raises:
            TypeError:
                name must be a string
                size must be a string
                customization must be a string
            ValueError:
                Size must be in [S,M,L]
        """
        # errors
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(size, str):
            raise TypeError("Size must be a string")
        if not size in ['S','M','L']:
            raise ValueError("Size must be in [S,M,L]")
        if custom:
            if not isinstance(custom, str):
                raise TypeError("Customization must be a string")
        # instance variables
        self.name: str = name
        self.size: str = size
        self.price: float = price_key[name][size]
        self.customization: str = custom

    def __str__(self) -> str:
        """Method to return a string representation of a Drink."""
        return f"{self.size} {self.name}, {self.customization} (${self.price})"

    #properties
    def name(self) -> str:
        """Returns the name of the drink"""
        return self.name
    def size(self) -> str:
        """Returns the size of the drink"""
        return self.size
    def price(self) -> float:
        """Returns the price of the drink"""
        return self.price
    def customization(self) -> str:
        """Returns the customizations entered by the user"""
        return self.customization
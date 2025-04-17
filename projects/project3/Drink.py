# File: Drink.py

# Imports

# Constants
price_key: dict[str,dict[str,float]] = {
    'Latte':{'S':4.5,'M':5,'L':5.5},
    'Matcha':{'S':5,'M':5.5,'L':6},
    'Hot Cocoa':{'S':3.5,'M':4,'L':4.5},
    'London Fog':{'S':14.75,'M':5.25,'L':5.75},
    'Red Bull Fusion':{'S':3.75,'M':4.25,'L':4.75}
}

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
        return f"{self.size} {self.name} {self.customization} ({self.price})"

    #properties
    def name(self) -> str:
        return self.name
    def size(self) -> str:
        return self.size
    def price(self) -> float:
        return self.price
    def customization(self) -> str:
        return self.customization
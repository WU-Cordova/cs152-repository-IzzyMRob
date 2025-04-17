# File: Drink.py

# Imports

# Implemetation

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
        self.price: int = price_key[name][size]
        self.customization: str = custom
    
    #properties
    @property
    def name(self) -> str:
        return self.name
    @property
    def size(self) -> str:
        return self.size
    @property
    def price(self) -> int:
        return self.price
    @property
    def customization(self) -> str:
        return self.customization


price_key: dict[str,dict[str,int]] = {
    'name':{'S':1,'M':1,'L':1}
}
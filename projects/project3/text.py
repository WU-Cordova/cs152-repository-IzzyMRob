# File: text.py

"""Contains all of the text that will not change when running the Bistro System"""

drinks: list = [
    "Latte", 
    "Matcha", 
    "Hot Cocoa", 
    "London Fog", 
    "Red Bull Fusion"
    ]

price_key: dict[str,dict[str,float]] = {
    'Latte':{'S':4.5,'M':5,'L':5.5},
    'Matcha':{'S':5,'M':5.5,'L':6},
    'Hot Cocoa':{'S':3.5,'M':4,'L':4.5},
    'London Fog':{'S':4.75,'M':5.25,'L':5.75},
    'Red Bull Fusion':{'S':3.75,'M':4.25,'L':4.75}
}

main_menu_text = [
    "Main Menu",
    "",
    "1. Display Menu",
    "2. Take New Order",
    "3. View Open Orders",
    "4. Mark Next Order as Complete",
    "5. Exit"
]
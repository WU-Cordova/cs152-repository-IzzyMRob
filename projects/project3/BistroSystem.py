# File: BistroSystem.py

# Imports
from datastructures.array import Array
from datastructures.circularqueue import CircularQueue
from projects.project3.Drink import Drink
from projects.project3.CustomerOrder import CustomerOrder

# Constants
welcome_text = "Welcome to the Bearcat Bistro!"
main_menu_text = [
    "Main Menu",
    "",
    "1. Display Menu",
    "2. Take New Order",
    "3. View Open Orders",
    "4. Mark Next Order as Complete",
    "5. Exit"
]

# Implementation

class BistroSystem():
    def __init__(self, menu:list):
        """Constructor function for the Day class.
        Args:
            menu (list[Drink]): The drinks available for the day
        Returns:
            None
        Raises:
            TypeError:
                name must be a string
        """
        # instance variables
        self.menu: list[str] = menu
        self.in_progress_orders: CircularQueue[CustomerOrder] = CircularQueue()
        self.completed_orders: Array[CustomerOrder] = Array(data_type=CustomerOrder)

    def start(self):
        print(welcome_text)
        self.disp_main_menu()

    def disp_main_menu(self):
        print("")
        multi_print(main_menu_text)
        choice = input("What would you like to do? ")
        if choice == '1':
            self.display_menu()
        elif choice == '2':
            self.disp_take_new_order()

    def disp_numbered_drinks(self):
        count = 0
        for drink in self.menu:
            count += 1
            print(f"{count}. {drink}")

    def display_menu(self):
        print("")
        self.disp_numbered_drinks()
        choice = input("Press 'o' to order or 'm' to go to the main menu.")
        if choice == 'm':
            self.disp_main_menu()
        elif choice == 'o':
            self.disp_take_new_order()

    def disp_take_new_order(self):
        print("")
        print("Starting new Order")
        cust_name = input("What is your name? ")
        current_order = CustomerOrder(cust_name)
        finished = False
        while not finished:
            self.disp_numbered_drinks()
            choice = input("Which drink would you like? ")
            name = self.menu[int(choice) - 1]
            size = input(f"What size do you want your {name}? (S/M/L) ").upper()
            customization = input(f"Please input any customizations to your {size} {name}. ")
            current_order.add(Drink(name, size, customization))
            print("")
            print("Your current order:")
            print(current_order)
            complete = input("Is this order complete? (Y/N)").upper()
            if complete =='Y':
                finished = True
        print(f"Your order is complete! Total price: ${current_order.get_total_price()}")
        self.in_progress_orders.enqueue(current_order)
        self.disp_main_menu()

def multi_print(text):
    for line in text:
        print(line)
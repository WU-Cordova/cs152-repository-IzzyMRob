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
        self.in_progress_orders: CircularQueue[CustomerOrder] = CircularQueue(10)
        self.completed_orders: Array[CustomerOrder] = Array(data_type=CustomerOrder)
        self.drink_counts = {
            "Latte": [0, 0],
            "Matcha": [0, 0], 
            "Hot Cocoa": [0, 0], 
            "London Fog": [0, 0], 
            "Red Bull Fusion": [0, 0]
        }

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
        elif choice == '3':
            self.disp_open_orders()
        elif choice == '4':
            self.disp_mark_order_complete()
        elif choice == '5':
            self.exit()

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
            self.drink_counts[name][0] += 1
            size = input(f"What size do you want your {name}? (S/M/L) ").upper()
            customization = input(f"Please input any customizations to your {size} {name}. ")
            drink = Drink(name, size, customization)
            self.drink_counts[name][1] += drink.price
            current_order.add(drink)
            print("")
            print("Your current order:")
            print(current_order)
            complete = input("Is this order complete? (Y/N)").upper()
            if complete == 'Y':
                finished = True
        print(f"Your order is complete! Total price: ${current_order.get_total_price()}")
        self.in_progress_orders.enqueue(current_order)
        self.disp_main_menu()

    def disp_open_orders(self):
        print("")
        print("Current Open Orders:")
        count = 0
        for order in self.in_progress_orders:
            count += 1
            print(f"{count}. {order}")
        choice = input("Press 'c' to mark an order as complete, or 'm' to go to the main menu.").upper()
        if choice == 'C':
            self.disp_mark_order_complete()
        elif choice == 'M':
            self.disp_main_menu()

    def disp_mark_order_complete(self):
        print("")
        print('Would you like to mark this order as complete?')
        print(self.in_progress_orders.front)
        choice = input("Press 'y' to complete this order, or 'm' to return to the main menu.").upper()
        if choice == 'Y':
            self.mark_next_complete()
            print("Marked as complete!")
            self.disp_main_menu()
        elif choice == 'M':
            self.disp_main_menu()

    def mark_next_complete(self):
        self.completed_orders.append(self.in_progress_orders.dequeue())

    def exit(self):
        print("")
        print("End of Day Report:")
        print("drink name - number sold - sales")
        for key,value in self.drink_counts.items():
            print (f"{key}: {value}")


def multi_print(text):
    for line in text:
        print(line)
# File: BistroSystem.py

# Imports
from datastructures.array import Array
from datastructures.circularqueue import CircularQueue
from projects.project3.Drink import Drink
from projects.project3.CustomerOrder import CustomerOrder
from projects.project3.text import main_menu_text, price_key

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
                menu must be an Array of strings
        """
        # errors
        if not isinstance(menu, Array):
            raise TypeError("Menu must be an Array")
        for item in menu:
            if not isinstance(item, str):
                raise TypeError("All items in menu must be strings")
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
        self.total_revenue: float = 0

    def start(self):
        """One-time call, prints initial welcome text and opens the main menu"""
        print("Welcome to the Bearcat Bistro!")
        self.disp_main_menu()

    def disp_main_menu(self):
        """Displays the main menu with 5 options for the user to take"""
        # blank line, print menu text
        print("")
        multi_print(main_menu_text)
        # lead to functions based on numbered user input
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
        """Displays a numbered menu of all 5 drinks available"""
        count = 0
        for drink in self.menu:
            count += 1
            print(f"{count}. {drink} (${price_key[drink]['M']})")

    def display_menu(self):
        """Option to display the menu from the main menu, can lead back to main menu or to take a new order"""
        # blank line, display menu
        print("")
        self.disp_numbered_drinks()
        # input to go to main menu or take an order
        choice = input("Press 'o' to order or 'm' to go to the main menu.")
        if choice == 'm':
            self.disp_main_menu()
        elif choice == 'o':
            self.disp_take_new_order()

    def disp_take_new_order(self):
        """Method to take a new order from the customer."""
        # blank line, starting text
        print("")
        print("Starting new Order")
        # get name, init CustomerOrdr object with it
        cust_name = input("What is your name? ")
        current_order = CustomerOrder(cust_name)
        # loop to add drinks as long as user wants to
        finished = False
        while not finished:
            # display drinks, get drink name and add to purchased count
            self.disp_numbered_drinks()
            choice = input("Which drink would you like? ")
            name = self.menu[int(choice) - 1]
            self.drink_counts[name][0] += 1
            # get size and customization
            size = input(f"What size do you want your {name}? (S/M/L) ").upper()
            customization = input(f"Please input any customizations to your {size} {name}. ")
            # create Drink, add price to total price and revenue, add drink to order
            drink = Drink(name, size, customization)
            self.drink_counts[name][1] += drink.price
            self.total_revenue += drink.price
            current_order.add(drink)
            # confirm order and option to add anoter drink or end
            print("")
            print("Your current order:")
            print(current_order)
            complete = input("Is this order complete? (Y/N)").upper()
            if complete == 'Y':
                finished = True
        # confirm order finished, give total price, back to main menu
        print(f"Your order is complete! Total price: ${current_order.get_total_price()}")
        self.in_progress_orders.enqueue(current_order)
        self.disp_main_menu()

    def disp_open_orders(self):
        """Displays all uncompleted orders"""
        # blank line, display all open orders
        print("")
        print("Current Open Orders:")
        count = 0
        for order in self.in_progress_orders:
            count += 1
            print(f"{count}. {order}")
        # input option to complete an order or return to main menu
        choice = input("Press 'c' to mark an order as complete, or 'm' to go to the main menu.").upper()
        if choice == 'C':
            self.disp_mark_order_complete()
        elif choice == 'M':
            self.disp_main_menu()

    def disp_mark_order_complete(self):
        """Method to mark an order as complete"""
        # blank line, conform order and mark as complete
        print("")
        print('Would you like to mark this order as complete?')
        print(self.in_progress_orders.front)
        choice = input("Press 'y' to complete this order, or 'm' to return to the main menu.").upper()
        # input option to mark as complete or return to manu
        if not self.in_progress_orders.empty:
            if choice == 'Y':
                self.mark_next_complete()
                print("Marked as complete!")
                self.disp_main_menu()
            elif choice == 'M':
                self.disp_main_menu()
        else:
            print("There are no open orders.")
            self.disp_main_menu()

    def mark_next_complete(self):
        """Removes front in progress order and adds it to completed orders"""
        self.completed_orders.append(self.in_progress_orders.dequeue())

    def exit(self):
        """Ends the run and displays an end of day summary"""
        print("")
        print("End of Day Report:")
        print("drink name - number sold - sales")
        for key,value in self.drink_counts.items():
            print (f"{key}: {value}")
        print(f"Total revenue today: ${self.total_revenue}")


def multi_print(text):
    """Helper function to print lists of strings easier"""
    for line in text:
        print(line)
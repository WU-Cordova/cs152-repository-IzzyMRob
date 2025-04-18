# File: program.py

# Imports
from projects.project3.BistroSystem import BistroSystem
from datastructures.array import Array

# Constants
drinks: list = ["Latte", "Matcha", "Hot Cocoa", "London Fog", "Red Bull Fusion"]

#Implementation

def main():

    menu:Array = Array(drinks)
    day = BistroSystem(menu)
    day.start()


if __name__ == '__main__':
    main()

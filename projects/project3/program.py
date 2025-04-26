# File: program.py

# Imports
from projects.project3.BistroSystem import BistroSystem
from datastructures.array import Array
from projects.project3.text import drinks

#Implementation

def main():
    """Main function to run the Bistro System"""
    menu:Array = Array(drinks)
    day = BistroSystem(menu)
    day.start()


if __name__ == '__main__':
    main()

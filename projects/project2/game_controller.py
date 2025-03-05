# File: game_controller.py

# Imports
from projects.project2.kbhit import KBHit
from projects.project2.cell import Cell
from projects.project2.grid import Grid

# Implementation

# GameController class
class GameController():
    
    def __init__(self):
        pass

    def run(self):
        #print the first grid
        print("Press q to quit.")

        #variables
        kbhit = KBHit()

        #start loop
        running = True
        while running:
            self.grid.display()
            sleep(1)
            if kbhit.kbhit():
                key =kbhit.getch()
            #generate next grid
                #iterate through grid
                #count neighbors
                #apply rules
            #store history
            #print grid
            #set grid = new grid

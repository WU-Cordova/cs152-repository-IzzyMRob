# File: game_controller.py

# Imports
from projects.project2.kbhit import KBHit
from projects.project2.cell import Cell
from projects.project2.grid import Grid

# Implementation

# GameController class
class GameController():
    
    def __init__(self, grid):
        self.grid: Grid = grid

    def run(self):
        print(self.grid)
        print("Press q to quit.")

        #variables
        kbhit = KBHit()

        #start loop
        running = True
        while running:
            self.grid.display()
            sleep(1)
            
            # check for quit
            if kbhit.kbhit():
                key =kbhit.getch()
                if key == "k":
                    print("You have quit.")
                    return
            

            #generate next grid
                #iterate through grid
                #count neighbors
                #apply rules
            #store history
            #print grid
            #set grid = new grid

# File: game_controller.py

# Imports
from projects.project2.kbhit import KBHit
from projects.project2.cell import Cell
from projects.project2.grid import Grid
from datastructures.array2d import Array2D
from projects.project2.igame_controller import IGameController, T
import time

# Implementation

# GameController class
class GameController(IGameController[T]):
    
    def __init__(self, grid:Grid, rows:int, cols:int, secs:int) -> None:
        self.grid: Grid = grid
        self.grid_1: Grid = None
        self.grid_2: Grid = None
        self.grid_3: Grid = None
        self.auto: bool = False
        self.rows: int = rows
        self.cols: int = cols
        self.seconds: int = secs

    def run(self) -> None:
        # initial prints, grid and help
        print("Press 'q' to quit or 'h' for help.")
        self.grid.display()
        #variables
        kbhit = KBHit()
        count = 0

        #start loop
        running:bool = True
        while running:
            # check for key press
            if kbhit.kbhit():
                key:str = kbhit.getch()
                # quit, stop running
                if key == "q":
                    print(f"You have quit after {count} generations.")
                    running = False
                    return
                # help, print help message
                elif key == "h":
                    print("Press 'q' to quit.")
                    print("Press 'a' to advance one generation.")
                    print("Press 's' to toggle automatic advancement.")
                # advance, more through one generation
                elif key == "a":
                    count += 1
                    print(f"You advanced to generation: {count}")
                    self.advance_generation()
                    running = self.check_end()
                #
                elif key == "s":
                    auto:bool = True
                    while auto:
                        count += 1
                        time.sleep(self.seconds)
                        print(f"You advanced to generation: {count}")
                        self.advance_generation()
                        running = self.check_end()
                        if kbhit.kbhit():
                            if kbhit.getch() == "s":
                                auto = False
                            elif kbhit.getch() == "q":
                                auto = False
                                running = False
        print(f"The game has ended after {count} generations.")
            
    def advance_generation(self) -> None:
        # store history
        self.grid_3 = self.grid_2
        self.grid_2 = self.grid_1
        self.grid_1 = self.grid
        # generate next grid and set it to current
        new_grid:Array2D = self.grid.next_generation()
        self.grid = Grid(self.rows, self.cols, new_grid)
        self.grid.display()


    def check_end(self) -> bool:
        # if all are the same
        if self.grid == self.grid_1 == self.grid_2:
            print("The grid has entered a repeating pattern, execution has stopped.")
            return False
        # if alternating pattern
        elif self.grid == self.grid_2 and self.grid_1 == self.grid_3:
            print("The grid has entered an alternating pattern, execution has stopped.")
            return False
        else:
            return True

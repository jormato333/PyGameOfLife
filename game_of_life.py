import os
import time

class Cel:
    def __init__(self, alive:bool=False):
        self.alive = alive
        self.neighbours = 0
        
    def cell_shape(self) -> str:
        return "o " if self.alive else "  "

class Grid:
    def __init__(self, initial_grid:list = [[]]):
        self.size_rows = len(initial_grid)
        self.size_cols = len(initial_grid[0])
        self.cels = []
        self.cels_next_gen = []
        
        try:
            for row in range(self.size_rows):
                self.cels.append([])
                self.cels_next_gen.append([])
                for col in range(self.size_cols):
                    self.cels[row].append(Cel(True) if initial_grid[row][col] == 1 else Cel())
                    self.cels_next_gen[row].append(Cel(True) if initial_grid[row][col] == 1 else Cel())
        except:
            print("[!]ERROR: All lines must have the same length")
            exit()
        
    
    def modify_grid(self, x:int, y:int, cel_status:bool=True):
        self.cels[x][y].alive = cel_status

    def count_neighbours(self, row, col):
        self.cels[row][col].neighbours = 0 
        if col > 0 and row > 0 and row < len(self.cels) - 1 and col < len(self.cels[row]) - 1:
            for i in range(3):
                if self.cels[row-1][col-1 + i].alive: self.cels[row][col].neighbours += 1
                if self.cels[row][col-1 + i].alive and i != 1: self.cels[row][col].neighbours += 1
                if self.cels[row+1][col-1 + i].alive: self.cels[row][col].neighbours += 1

    def update_cel(self, row, col):
        if self.cels[row][col].alive: 
            if self.cels[row][col].neighbours in [2,3]:
                self.cels_next_gen[row][col].alive = True
                return

        elif self.cels[row][col].neighbours == 3:
            self.cels_next_gen[row][col].alive = True
            return

        self.cels_next_gen[row][col].alive = False
        return
    
    def print_cel(self, row, col):
        if row == 0 and col == 0:
            os.system("cls")

        print(self.cels[row][col].cell_shape(), end="")
        if col == len(self.cels[row]) - 1:
            print()

    def game_over(self,row,col):
        return self.cels[row][col].alive

    def play_game(self):
        keep_playing = False
        for row in range(len(self.cels)):
            for col in range(len(self.cels[row])):              
                self.count_neighbours(row, col)
                self.update_cel(row, col)
                self.print_cel(row, col)
                if self.game_over(row, col) or self.cels == self.cels_next_gen: keep_playing = True
        for row in range(len(self.cels)):
            for col in range(len(self.cels[row])):
                self.cels[row][col].alive = self.cels_next_gen[row][col].alive
        return keep_playing
                

template1 = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0],
[0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0],
[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0],
[0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0],
[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]
template2 =[
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
[0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

if input("[+] Select template 1 or 2 (1,2): ") == "1":
    grid = Grid(template1)
else:
    grid = Grid(template2)

play = True

while play:

    play = grid.play_game()
    time.sleep(0.1)

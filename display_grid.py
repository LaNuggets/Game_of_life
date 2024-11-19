import os 

def display_grid(grid):
    os.system('clear')
    for i in grid:
        print(" ".join(str(j) for j in i))
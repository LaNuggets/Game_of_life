import random
import os 

def generate_grid():

    grid_size = input("Enter the grid size: ")

    while not grid_size.isnumeric():
        grid_size = input("Enter a number to indicate grid size: ")

    while int(grid_size) > 55 or int(grid_size) < 3:
        print("Please choose a number between 3 and 55")
        grid_size = input("Enter the grid size: ")
        
    components = [0, 1]
    grid = [[random.choice(components) for _ in range(int(grid_size))] for _ in range(int(grid_size))]

    return grid

def display_grid(grid, living_cell_symbol='⬛', dead_cell_symbol='⬜'):
    os.system('clear')
    for i in grid:
        replace_symbole = [living_cell_symbol if x == 1 else dead_cell_symbol for x in i]
        print("".join(replace_symbole))

frame = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1),(1, -1), (1, 0), (1, 1)]

def cell_state(grid):
    actual_grid = [row[:] for row in grid]
    live_cells = 0

    for i, value in enumerate(grid):
        for j,_ in enumerate(value):
            for x_frame, y_frame in frame:
                x_direction = i + x_frame
                y_direction = j + y_frame

                if 0 <= x_direction < len(grid) and 0 <= y_direction < len(grid[0]):
                    if grid[x_direction][y_direction] == 1:
                        live_cells += 1 

            if live_cells == 3:
                actual_grid[i][j] = 1
            elif live_cells == 2:
                actual_grid[i][j] = grid[i][j]
            else:
                actual_grid[i][j] = 0
            live_cells = 0

    return actual_grid

def scan_history(grid, history, count):
    count += 1
    if count >= 2:
        if grid in history:
            return count, True
    return count, False

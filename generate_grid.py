import random

def generate_grid():
    grid_size = input("Enter the grid size: ")
    components = [0, 1]

    grid = [[random.choice(components) for _ in range(int(grid_size))] for _ in range(int(grid_size))]

    return grid

import random

def generate_grid():
    length = input("enter length: ")
    width = input("enter width: ")
    components = [0, 1]

    grid = [[random.choice(components) for _ in range(int(length))] for _ in range(int(width))]

    return grid

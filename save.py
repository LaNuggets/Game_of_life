import json

def save_grid(grid):
    with open('grid.json', 'w') as f:
        json.dump({'grid' : grid}, f)

def load_grid():
    with open('grid.json', 'r') as f:
        data = json.load(f)

    return data['grid'] 
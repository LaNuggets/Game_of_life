import json

def save_grid(grid):
    with open('history.json', 'w') as f:
        json.dump({'grid' : grid}, f)

def load_grid():
    with open('history.json', 'r') as f:
        data = json.load(f)

    return data['grid'] 
import grid as gd
import prompt as pr
import time

def main():
    history = []
    count = 0
    cycle_start = 0
    is_cycle = False
    grid = pr.menu()
    history.append(grid)
    
    while True:
        gd.display_grid(grid)
        print(f"You are currently at turn {count}")
        if is_cycle:
            print(f"Cycle detected at turn {cycle_start}, you are at turn {count}")
        pr.ask_user(grid)
        grid = gd.cell_state(grid)
        cycle_start, count, is_cycle = gd.scan_history(cycle_start, grid, history, count)
        history.append(grid)

main()
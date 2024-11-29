import grid as gd
import prompt as pr
import time
import variables as v

def main():
    grid = pr.menu()
    v.history.append(grid)
    
    while True:
        gd.display_grid(grid)
        print(f"You are currently at turn {v.count}")
        if v.is_cycle:
            print(f"Cycle detected at turn {v.cycle_start}, you are at turn {v.count}")
        pr.ask_user(grid)
        grid = gd.cell_state(grid)
        v.cycle_start, v.count, v.is_cycle = gd.scan_history(v.cycle_start, grid, v.history, v.count)
        v.history.append(grid)

main()
import grid as gd
import prompt as pr
import time


def main():
    history = []
    count = 0
    is_cycle = False
    pr.menu()
    grid = gd.generate_grid()
    history.append(grid)
    
    while True:
        grid = gd.cell_state(grid)
        count, is_cycle = gd.scan_history(grid, history, count)
        history.append(grid)
        gd.display_grid(grid)
        print(count)
        if is_cycle:
            print("cycle detected")
        pr.ask_user()

main()
import grid as gd
import prompt as pr
import time
import variables as v

def main():
    try:
        grid = pr.menu()
        v.history.append(grid)
        
        while True:
            gd.display_grid(grid)
            print(f"\033[1;35mYou are currently at turn {v.count}\033[0m")
            if v.is_cycle:
                print(f"\033[1;33mCycle detected at turn {v.cycle_start} !\033[0m")
            pr.ask_user(grid)
            grid = gd.cell_state(grid)
            v.cycle_start, v.count, v.is_cycle = gd.scan_history(v.cycle_start, grid, v.history, v.count)
            v.history.append(grid)
    except:
        print('\n\n\033[1;31mShutting Down!\033[0m')
main()
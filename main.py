import generate_grid as gd
import display_grid as dg
import cell_state as cs
import menu as m
import ask_user as au

def main():
    m.menu()
    grid = gd.generate_grid()
    while True:
        dg.display_grid(grid)
        grid = cs.cell_state(grid)
        dg.display_grid(grid)
        au.ask_user()

main()
import os
import save as sv
import grid as gd

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;32mWelcome to the Game of Life !\033[0m\n")
    print('\033[1;32mThis is an auto generate game.\033[0m\n')

    while True:
        user_response = input('\033[1;34mLoad the previous grid, y/n: \033[0m')
        if user_response == 'y':
            try:
                grid = sv.load_grid()
            except:
                print("\033[1;31mThere is no game history! Starting a new game.\033[0m")
                grid = gd.generate_grid()
            return grid
        elif user_response == 'n':
            grid = gd.generate_grid()
            return grid
        elif user_response == "q":
           exit(0)
        else:
            print('\033[1;31mWrong key pressed. Please press "y" or "n"\033[0m')

def ask_user(grid):
    while True:
        user_response = input('\033[1;34mPress "Enter" to continue or "q" to exit: \033[0m')
        if user_response == "q":
           sv.save_grid(grid)
           exit(0)
        elif user_response == "":
           return
        else:
            print('\033[1;31mWrong key pressed. Please press "Enter" or "q"\033[0m')

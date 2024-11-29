import os
import save as sv
import grid as gd

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Game of Life !\n")
    print('This is an auto generate game based on your choices.')

    while True:
        user_response = input('Load the previous grid, y/n: ')
        if user_response == 'y':
            try:
                grid = sv.load_grid()
            except:
                print("There is no game history! Starting a new game.")
                grid = gd.generate_grid()
            return grid
        elif user_response == 'n':
            grid = gd.generate_grid()
            return grid
        elif user_response == "q":
           exit(0)
        else:
            print('Wrong key pressed. Please press "y" or "n"')

def ask_user(grid):
    while True:
        user_response = input('Press "Enter" to continue or "q" to exit: ')
        if user_response == "q":
           sv.save_grid(grid)
           exit(0)
        elif user_response == "":
           return
        else:
            print('Wrong key pressed. Please press "Enter" or "q"')
import os

def menu():
    os.system('clear')
    print("Welcome to the Game of Life !\n")
    print('This is an auto generate game base on your choices \n')
    print('At any moment press\'q\' to exit')

def ask_user():
    while True:
        user_responce = input('Press "Enter" to continue or "q" to exit: ')
        if user_responce == "q":
           exit(0)
        elif user_responce == "":
           return
        else:
            print('Wrong ky pressed. Please presse "Enter" or "q"')
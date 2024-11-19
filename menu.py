import os


def menu():
    os.system('clear')
    print("Welcome to the Game of Life !\n")
    print('This is an auto generate game base on your choices \n')
    print('At any moment press\'q\' to exit')



def turn():
    user_responce = ""
    while(user_responce != 'q' or user_responce != 'enter'):
        user_responce = input('Do you want to continue, press "Enter" to continue or "q" to finish: ')
        if user_responce == 'q':
            exit(1)
        elif user_responce == '\n':
            continue
        else:
            print('Wrong key pressed. Please use "Enter" or "q": ')

turn()

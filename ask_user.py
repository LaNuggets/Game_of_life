def ask_user():
    while True:
        user_responce = input('Press "Enter" to continue or "q" to exit: ')
        if user_responce == "q":
           exit(0)
        elif user_responce == "":
           return
        else:
            print('Wrong ky pressed. Please presse "Enter" or "q"')
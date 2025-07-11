def select_valid_option(message, options):
    """
    Recieves a message to show in the input and a string of the options allowed. Iterates until a valid input is given.
    """
    while True:
        option = input(message)
        if option in list(options):
            return option
        else: 
            print("Please, insert a valid option")
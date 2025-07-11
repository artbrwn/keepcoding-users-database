from users_classes import Admin, Client

users_database = {"admin": Admin("admin", "admin1234"), "client1": Client("client1", "123456")}


def main():
    print_login_menu()
    while True:
        option = select_valid_option("What do you want to do?: ", "12")
        if option == "1":
            logged_user = login_user()
            while True:
                logged_user.menu()
                option = select_valid_option("What do you want to do?: ", "1234" if isinstance(logged_user, Admin) else "123")
        elif option == "2":
            break

def print_login_menu():
    print("Welcome to the App")
    print("Options")
    print("1 - Login")
    print("2 - Quit")

def select_valid_option(message, options):
    while True:
        option = input(message)
        if option in list(options):
            return option
        else: 
            print("Please, insert a valid option")

def login_user():
    nickname = input("User: ")
    password = input("Password: ")
    if nickname and nickname in users_database:
        if password == users_database[nickname].password:
            print("Logged in")
            return users_database[nickname]
        else:
            print("Incorrect password, please try again.")

    else:
        print(f"{nickname} is not a registered user, please try again.")


if __name__ == "__main__":
    main()
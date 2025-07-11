from users_classes import Admin, Client, users_database
from utils import select_valid_option


def main():
    print("Welcome to the App")
    while True:
        print_login_menu()
        option = select_valid_option("What do you want to do?: ", "12")
        if option == "1":
            logged_user = login_user()
            if logged_user:
                logged_user.menu()
        elif option == "2":
            break

def print_login_menu():
    print("\nOptions")
    print("1 - Login")
    print("2 - Exit the app")

def login_user():
    """
    Asks for user and password, if a valid nickname and password are given returns the user.
    """
    print("\nLogging in")
    username = input("User: ")
    password = input("Password: ")
    if username and username in users_database:
        if password == users_database[username].password:
            print("Logged in")
            return users_database[username]
        else:
            print("Incorrect password, please try again.")

    else:
        print(f"{username} is not a registered user, please try again.")

if __name__ == "__main__":
    main()
class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password

class Admin(User):
    def menu(self):
        print(f"You are logged as {self.user}, admin.")
        print("Options:")
        print("1 - View list of users")
        print("2 - Sign up a new user")
        print("3 - Remove an existing user")
        print("4 - Log out")

class Client(User):
    def menu(self):
        print(f"You are logged as {self.user}, client.")
        print("Options:")
        print("1 - Show products")
        print("2 - Buy a product")
        print("3 - Log out")

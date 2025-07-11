from databases import products_database
from utils import select_valid_option


class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.category = "Admin" if isinstance(self, Admin) else "Client"

class Admin(User):
    def menu(self):
        while True:
            print(f"\nYou are logged as {self.user}, admin.")
            print("Options:")
            print("1 - View list of users")
            print("2 - Sign up a new user")
            print("3 - Remove an existing user")
            print("4 - Log out")

            option = select_valid_option("What do you want to do?: ", "1234")

            if option == "1":
                self.view_list_of_users()
            elif option == "2":
                self.create_user()
            elif option == "3":
                auto_remove = self.remove_user()
                if auto_remove:
                    print("You logged out.")
                    break
            elif option == "4":
                print("You logged out")
                break

    def view_list_of_users(self):
        print("\nList of users:")
        print(f"{'Username':^17} | {'Role':^17} ")
        print("-"*34)
        for user in users_database.values():
            print(f"{user.user:^17} | {user.category:^17}")
    
    def create_user(self):
        while True:
            user = input("Please insert username: ")
            if user in users_database:
                print(f"{user} is already registered, please select a different username")
            else:
                password = input("Insert a password for this user: ")
                role = select_valid_option("Choose role [1] admin or [2] client: ", "12")
                if role == "1":
                    users_database[user] = Admin(user, password)
                    break
                else:
                    users_database[user] = Client(user, password)
                    break

    def remove_user(self):
        self_remove = False
        user = input("Please insert the username of the user you want to remove: ")
        if user in users_database:
            check = select_valid_option(f"Are you sure you want to remove {user}? [Y/n]: ", "yn").lower()
            if check == "y":
                users_database.pop(user)
                print(f"{user} was removed.")
                if user == self.user:
                    self_remove = True

        else:
            print(f"{user} not in database.")
        return self_remove

class Client(User):

    def menu(self):
        while True:
            print(f"\nYou are logged as {self.user}, client.")
            print("Options:")
            print("1 - Show products")
            print("2 - Buy a product")
            print("3 - Log out")

            option = select_valid_option("What do you want to do?: ", "123")

            if option == "1":
                self.list_products()
            elif option == "2":
                self.buy()
            elif option == "3":
                print("You logged out. \n")
                break

    def list_products(self):
        print("\nList of products:")
        print(f"{'ID':^3} | {'Name':^10} | {'Size':^6} | {'Stock left':^11} | {'Price':^7}")
        print("-" * 50)

        for product_id, product_info in products_database.items():
            print(f"{str(product_id):^3} | {product_info['name']:^10} | {product_info['size']:^6} | {str(product_info['stock']):^11} | {str(product_info['price']):^7}€")
    
    def buy():
        pass

users_database = {"admin": Admin("admin", "admin1234"), "client1": Client("client1", "123456")}

from databases import products_database

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

    def list_products(self):
        print("List of products:")
        print(f"{'ID':^3} | {'Name':^10} | {'Size':^6} | {'Stock left':^11} | {'Price':^7}")
        print("-" * 50)

        for product_id, product_info in products_database.items():
            print(f"{str(product_id):^3} | {product_info['name']:^10} | {product_info['size']:^6} | {str(product_info['stock']):^11} | {str(product_info['price']):^7}")





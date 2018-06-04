from databaseconnector import DatabaseConnector

class CheckoutSystem():
    def __init__(self):
        self.connector = DatabaseConnector()

    def get_product_id(self):
        return self.connector.get_query("SELECT id, name, amount_in_stock FROM products")
    
    def get_product_name(self, productid):
        return self.connector.get_query("SELECT name FROM products WHERE id = {}".format(productid))[0][0]

    def get_amount_in_cartridge(self, productid):
        return self.connector.get_query("SELECT amount_in_cartridge FROM productsinshelve WHERE product_id = {}".format(productid))[0][0]

    def decrement_product(self, productid):
        value = int(self.connector.get_query("SELECT amount_in_cartridge FROM productsinshelve WHERE product_id = {}".format(productid))[0][0]) - 1
        self.connector.execute_query("UPDATE productsinshelve SET amount_in_cartridge = {} WHERE product_id = {}".format(value, productid))

    def increment_product(self, productid):
        value = int(self.connector.get_query("SELECT amount_in_cartridge FROM productsinshelve WHERE product_id = {}".format(productid))[0][0]) + 1
        self.connector.execute_query("UPDATE productsinshelve SET amount_in_cartridge = {} WHERE product_id = {}".format(value, productid))

class CheckoutInterface():
    """A CMD interface to interact easily with the checkout system. This is used for demo's or when you want to change data using the CMD"""
    def __init__(self, checkoutSystem):
        self.checkoutSystem = checkoutSystem
        self.run()

    def run(self):
        while True:
            inp = input("input command: ")
            inpsplit= inp.split(" ")

            if inp == "productlist":
                product_list = self.checkoutSystem.get_product_id()
                print("\nproducts: ")
                for product_entry in product_list:
                    print("   id:", product_entry[0], "name:", product_entry[1], "in stock:", product_entry[2])
            elif inpsplit[0] == "cartridgeamount":
                print(self.checkoutSystem.get_product_name(inpsplit[1]), ": ", self.checkoutSystem.get_amount_in_cartridge(inpsplit[1]), sep='')
            elif inpsplit[0] == "incrproduct":
                self.checkoutSystem.increment_product(inpsplit[1])
            elif inpsplit[0] == "decrproduct":
                self.checkoutSystem.decrement_product(inpsplit[1])
            elif inp == "help":
                print("commands: \n    productlist\n    cartridgeamount [productid]\n    incrproduct [productid]\n    decrproduct [productid]\n    help\n    exit\n")
            elif inp == "exit":
                break

checkout = CheckoutInterface(CheckoutSystem())

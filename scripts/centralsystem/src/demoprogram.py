from databaseconnection import DatabaseConnection
import methods

class demoController:
	def __init__(self):
		self.db = DatabaseConnection()

	def empty_tray(self, product_id, shelf_id):
		self.db.execute_query('UPDATE productsinshelve SET amount_in_cartridge = 0 where product_id = {} AND shelf_id = {}'.format(product_id, shelf_id))

	def fill_tray(self, product_id, shelf_id):
		cartridge_amount = self.db.get_query('SELECT amount_per_cartridge FROM products WHERE id = {}'.format(product_id))[0][0]
		self.db.execute_query('UPDATE productsinshelve SET amount_in_cartridge = {} WHERE product_id = {} AND shelf_id = {}'.format(cartridge_amount, product_id, shelf_id))

	def change_stock(self, product_id, amount):
		self.db.execute_query('UPDATE products SET amount_in_stock = {} WHERE id = {}'.format(amount, product_id))

	def get_product_data(self):
		product_array = self.db.get_query('SELECT product.id, product.name, product.amount_in_stock, productsinshelve.shelf_id, productsinshelve.amount_in_cartridge FROM products LEFT JOIN productsinshelve ON products.id = productsinshelve.product_id')
		for product in product_array:
			product = 'id: {} shelfid: {} name: {} in stock: {} in cartridge: {}'.format(product[0], product[3], product[1], product[2], product[4])
		return product_array

	def run(self):
		while True:
			inp = input('input command: ')
			inpsplit= inp.split(' ')

			if inp == 'list':
				methods.print_list('products:', self.get_product_data())
			elif inpsplit[0] == 'et':
				self.empty_tray(inpsplit[1], inpsplit[2])
			elif inpsplit[0] == 'ft':
				self.fill_tray(inpsplit[1], inpsplit[2])
			elif inpsplit[0] == 'cs':
				self.decrement_product(inpsplit[1], inpsplit[2])
			elif inp == 'help':
				commands = ['productlist', 'et [productid] [shelfid] (empty tray)', 'ft [productid] [shelfid] (fill tray)', 'cs [productid] [amount] (change amount in stock)', 'help', 'exit']
				methods.print_list('available commands:', commands)
			elif inp == 'exit':
				break
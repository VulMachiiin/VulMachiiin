from databaseconnector import DatabaseConnector

class WeightedGraph():
	"""docstring for WeightedGraph"""

	def __init__(self, db_connector):
		self.db_connector = db_connector

	def get_list(self):
		query_string = '''SELECT * FROM products'''
		values = self.db_connector.get_query(table_ref, query_string)

	def temp_list(self):


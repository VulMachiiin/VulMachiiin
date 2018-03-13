
### WATCHOUT OBSELETE!!!!

import sqlite3
import os.path
import os


# products = id | name | amountinstock | cartridgetype | amountpercartridge
# catridgeinfo = id | cartridgetype | amountpercartridge #

#sets up the whole database if there is no instance of the database already

def convert_user_input(message, error_message, type_to_compare):
	while True:
		output = input(message)
		if type_to_compare == int:
			try:
				output = int(output)
			except Exception as e:
				output = None
		else: #TODO now only handles int and str
			try:
				output = str(output)
			except Exception as e:
				output = None

		if type(output) is type_to_compare:
			return output
		else:
			print(error_message)

def clearterminal():
	os.system('cls' if os.name == 'nt' else 'clear')

def display_database():
	print('##########################################\n',
	  	  '#             DISPLAY TABLES             #\n',
	  	  '##########################################\n',
	  	  '# {:^38} #\n'.format('products'),
	  	  '##########################################\n',
	  	  end='', sep='')
	db = sqlite3.connect(DATABASE_PATH)
	cursor = db.cursor()
	cursor.execute('PRAGMA table_info("products")') #TODO print all tables
	columns = cursor.fetchall()
	print('# {0} | {1} | {2} | {3} | {4}'.format(columns[0][1], columns[1][1], columns[2][1], columns[3][1], columns[4][1]))

	cursor.execute('''SELECT * FROM products''')
	all_entries = cursor.fetchall()
	for entry in all_entries:
		print('# {0} | {1} | {2} | {3} | {4}'.format(entry[0], entry[1], entry[2], entry[3], entry[4]))

	print('#')
	db.close()

def add_entry():
	print('##########################################\n',
		  '#               ADD ENTRY                #\n',
		  '##########################################\n',
		  end='', sep='')
	db = sqlite3.connect(DATABASE_PATH)
	cursor = db.cursor()
	table_to_edit = select_table()
	print('###')

	cursor.execute('PRAGMA table_info({0})'.format(TABLE_NAMES[table_to_edit]))	
	column_info = cursor.fetchall()

	entry_data = []
	for column_item in column_info:
		print('# column name: {0}	column type: {1}'.format(column_item[1], column_item[2])) if column_item[5] == 0 else print('# column name: {0}	column type: {1} PRIMARY KEY'.format(column_item[1], column_item[2]))
		if column_item[1] == 'INTEGER':
			entry_data.append(convert_user_input('# value: ', '# not an int', int))
		else: #TODO: change this incase some other value then string or integer is wanted
			entry_data.append(convert_user_input('# value: ', '# not a string', str))

	database_add_entry(table_to_edit, entry_data)

	db.close()	
	


def select_table():
	table_option_counter = 0
	print('##########################################\n'
		  '#   choose the table you want to edit    #\n',
		  '##########################################\n',
		  end='', sep='')
	for table_name in TABLE_NAMES:
		table_option_counter += 1
		print('# {0}) {1}'.format(table_option_counter, table_name))

	print('###')
	while True:
		input_choice = convert_user_input('# choice: ', '# try a number 1-{0}'.format(table_option_counter), int)
		if input_choice <= table_option_counter and input_choice >= 1:
			return input_choice - 1
		else:
			print('# try a number 1-{0}'.format(table_option_counter))

def manage_database():
	clearterminal()
	input_choice = 1
	while True:
		#only print if typed in a valid choice and went into another function
		if input_choice >= 1 and input_choice <= 3:
			print('##########################################\n',
				  '#        DATABASE MANAGER OPTIONS        #\n',
				  '##########################################\n',
				  '# 1) display entries                     #\n',
				  '# 2) add entry                           #\n',
				  '# 3) remove entry                        #\n',
				  '# 4) exit                                #\n',
				  '##########################################\n',
				  end='', sep='')
		input_choice = convert_user_input('# choice: ', '# try a number 1-4', int)
		if input_choice == 1:
			print('#')
			display_database()
		elif input_choice == 2:
			print('#')
			add_entry()
		elif input_choice == 3:
			print('#')
			remove_entry()
		elif input_choice == 4:
			print('#')
			break
		else:
			print('# try a number 1-4')

#creates database if no existing database is found
if not os.path.isfile(DATABASE_PATH):
	setupdatabase()

manage_database()
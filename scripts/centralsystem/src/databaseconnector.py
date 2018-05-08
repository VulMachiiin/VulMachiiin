import MySQLdb
import math

class DatabaseConnector():
    """Class used for connecting with the database. Connecting without this class is heavily discouraged.

       NOTE THAT THIS IS JUST FOR OUR DATABASE DONT USE ON OTHER DATABASES"""
    #DATABASE_PATH = '../data/vulmachiiin_database.db'
    TABLE_NAMES = ('products', 'shelves', 'productsinshelve', 'paths', 'shelveonpaths', 'pathconnections')

    def __init__(self):
        self.setup_connection()

    def setup_connection(self):
        db = MySQLdb.connect(host="localhost",
                     user='vulmachiiin',
                     passwd='V0etInM0nd!',
                     db='vulmachiiin')
        print('connected')
        cursor = db.cursor()
        #cursor.execute('''SELECT 1 FROM products LIMIT 1;''')
        #results = cursor.fetchall()
        """results_formatted = []
        for item in results:
            results_formatted.append(item[0])

        if not set(self.TABLE_NAMES) <= set(results_formatted):
            self.setup_database()"""

    def setup_database(self):
        db = MySQLdb.connect(host="localhost",
                     user='vulmachiiin',
                     passwd='V0etInM0nd!',
                     db='vulmachiiin')
        print('connected')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER, 
                                                               name TEXT NOT NULL DEFAULT "placeholder", 
                                                               amount_in_stock INTEGER NOT NULL DEFAULT 0, 
                                                               cartridge_type INTEGER NOT NULL DEFAULT 1, 
                                                               amount_per_cartridge INTEGER NOT NULL DEFAULT 0,
                                                               PRIMARY KEY (id))''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS shelves (id INTEGER,
                                                              size_horizontal INTEGER NOT NULL DEFAULT 1,
                                                              size_vertical INTEGER NOT NULL DEFAULT 3,
                                                              PRIMARY KEY (id))''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS productsinshelve (product_id INTEGER,
                                                                       shelf_id INTEGER,
                                                                       x_coordinate INTEGER NOT NULL,
                                                                       y_coordinate INTEGER NOT NULL,
                                                                       PRIMARY KEY (product_id, shelf_id),
                                                                       FOREIGN KEY (product_id) REFERENCES products (id)
                                                                       ON DELETE CASCADE ON UPDATE NO ACTION,
                                                                       FOREIGN KEY (shelf_id) REFERENCES shelves (id)
                                                                       ON DELETE CASCADE ON UPDATE NO ACTION)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS nodes (id INTEGER,
                                                            shelve_id INTEGER,
                                                            PRIMARY KEY(id)
                                                            FOREIGN KEY (shelv,e_id) REFERENCES shelves (id))''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS shelveonpaths (shelve_id INTEGER,
                                                                    path_id INTEGER,
                                                                    PRIMARY KEY (shelve_id, path_id),
                                                                    FOREIGN KEY (shelve_id) REFERENCES shelves (id)
                                                                    ON DELETE CASCADE ON UPDATE NO ACTION,
                                                                    FOREIGN KEY (path_id) REFERENCES paths (id)
                                                                    ON DELETE CASCADE ON UPDATE NO ACTION)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS edges (edge_id INTEGER PRIMARY KEY,
                                                            node_one_id INTEGER,
                                                            node_two_id INTEGER,
                                                            weight INTEGER NOT NULL,
                                                            FOREIGN KEY (node_one_id) REFERENCES paths (id)
                                                            ON DELETE CASCADE ON UPDATE NO ACTION,
                                                            FOREIGN KEY (node_two_id) REFERENCES paths (id)
                                                            ON DELETE CASCADE ON UPDATE NO ACTION,
                                                            CHECK (node_one_id <> node_two_id),
                                                            #CONTSTRAINT UNIQ_EDGE UNIQUE (node_one_id, node_two_id)
                                                            )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS directions()''')

        db.commit()
        print('succesfully made missing tables')
        db.close()

    def get_table_reference(self, table_name):
        for i in range(length(TABLE_NAMES) - 1):
            if table_name == TABLE_NAMES[i]:
                return i

    def add_entry(self, table_reference, data_list):
        ddb = MySQLdb.connect(host="localhost",
                     user='vulmachiiin',
                     passwd='V0etInM0nd!',
                     db='vulmachiiin')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO {0} VALUES ({1})'''.format(self.TABLE_NAMES[table_reference], ', '.join('?' for data in data_list)), (data_list))
        db.commit()
        db.close()

    # removes one entry from the table. the PK_tuple should look the following if there is a combined primary key: ((PK_one_name, PK_two_name, ...),(PK_one_value, PK_two_value, ...)) otherwise like following: ((PK_name, ),(PK_value, ))
    def remove_entry(self, table_reference, PK_tuple):
        db = MySQLdb.connect(host="localhost",
                     user='vulmachiiin',
                     passwd='V0etInM0nd!',
                     db='vulmachiiin')
        cursor = db.cursor()
        if PK_tuple[0].length == 1:
                cursor.execute('''DELETE FROM {0} WHERE {1} = ?'''.format(self.TABLE_NAMES[table_reference], PK_value[0]), (PK_value[1], ))
        else:
            string_to_input = ''
            for item in PK_tuple[0]:
                string_to_input += item + ' = ? AND '
            string_to_input = string_to_input[:(len(string_to_input) - 5)]
            cursor.execute('''DELETE FROM {0} WHERE {1}'''.format(self.TABLE_NAMES[table_reference], string_to_input), (PK_value[1]))
        db.commit()
        db.close()

    # TODO think of how to make this safer and more modular for other classes to request certain data
    def get_query(self, query):
        db = MySQLdb.connect(host="localhost",
                     user='vulmachiiin',
                     passwd='V0etInM0nd!',
                     db='vulmachiiin')
        cursor = db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        db.close()
        return results
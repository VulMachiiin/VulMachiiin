import MySQLdb
import math

class DatabaseConnector():
    """Class used for connecting with the database. Connecting without this class is heavily discouraged.

       NOTE THAT THIS IS JUST FOR OUR DATABASE DONT USE ON OTHER DATABASES"""

    def __init__(self):
        self.db = self.setup_connection()
        print('connected')

    def __del__(self):
        self.db.close()

    def setup_connection(self):
        return MySQLdb.connect(host="localhost",
                               user='vulmachiiin',
                               passwd='V0etInM0nd!',
                               db='vulmachiiin')

    def get_query(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    def execute_query(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        self.db.commit()

    # elegant pairing function by matthew szudzik
    def elegant_pair(self, coor_tuple):
        coor_tuple_x = coor_tuple[0]
        coor_tuple_y = coor_tuple[1]
        return (coor_tuple_x * coor_tuple_x + coor_tuple_y) if (coor_tuple_x >= coor_tuple_y) else (coor_tuple_y * coor_tuple_y + coor_tuple_x)

    def elegant_unpair(self, z):
        sqrtz = math.floor(math.sqrt(z))
        sqz = sqrtz * sqrtz
        return (sqrtz, z - sqz - sqrtz) if ((z - sqz) >= sqrtz) else (z - sqz, sqrtz)

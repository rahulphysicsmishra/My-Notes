"""Database connection management using context manager

Let's create a simple database connection management system. The
number of database connections that can be opened at a time is
also limited(just like file descriptors). Therefore context managers
are helpful in managing connections to the databse as there could
be chances that the programmer may forget to close the connection.
"""

# Python program shows the connection management for MongoDB

import mysql.connector as connector
from settings import DATABASE


class Cursor:
    def __init__(self,
                 host = DATABASE.get('HOST'),
                 user = DATABASE.get('USER'),
                 password = DATABASE.get('PASSWORD'),
                 db_name = DATABASE.get('NAME'),
                 driver = connector, ):
        self.driver = driver
        self.connection = self.driver.connect(
            host = host,
            user = user,
            password = password,
            database = db_name )
        self.cursor = self.connection.cursor()


    def __iter__(self):
        for item in self.cursor:
            yield item


    def __enter__(self):
        return self.cursor


    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()




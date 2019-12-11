import sqlite3
import datetime

"""
Function to connect to the database
"""


def connect_to_database():
    connection = sqlite3.connect('datas.db')
    print("Connected to SQLite")
    return connection


"""
Function to create a new table
"""


def create_table():
    # Connect to the database
    c = connect_to_database()
    cursor = c.cursor()
    # Query to create a table in the database
    sqlite_create_table_query = '''CREATE TABLE directory
                                            (name text, date current_date , signature text, modifiedDate timestamp);'''
    # Execute the create table query
    # And create a database named "directory"
    cursor.execute(sqlite_create_table_query)


"""
Function to add a new record in the directory table
"""


def add_directory(date, name, signature):
    try:
        # Connect to the database
        c = connect_to_database()
        cursor = c.cursor()

        # Query to insert details in directory table
        sqlite_insert_with_param = """INSERT INTO 'directory'
                                        ('date', 'name', 'signature') 
                                        VALUES (?, ?, ?);"""

        # Save in a tuple the data coming from the parameter
        data_tuple = (date, name, signature)

        # Execute the insert query
        # And create a new record in the directory table
        cursor.execute(sqlite_insert_with_param, data_tuple)

        # Commit to save the changes
        c.commit()
        print("New record added successfully \n")

        # Query to get directory details
        sqlite_select_query = """SELECT name, date, signature FROM directory WHERE name = ?"""

        cursor.execute(sqlite_select_query, ("YYYYRRRRMMMMM",))
        records = cursor.fetchall()
        print(records)

        for row in records:
            directory = row[0]
            date = row[1]
            signature = row[2]
            print("The directory: ", directory, " was added on ", date)
            print("The signature is: ", signature)

        cursor.close()

    except sqlite3.Error as error:
        print("Error while processing with SQLite", error)
    finally:
        if (c):
            c.close()
            print("SQLite connection is closed")


add_directory(datetime.datetime.now(), "YYYYRRRRMMMMM", "FDKJFDHJGBFDGFDG546546546825D4F5S6")

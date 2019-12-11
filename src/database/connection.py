import sqlite3
import datetime


def addDirectory(date, name, signature):
    try:
        connection = sqlite3.connect('data.txt')
        c = connection.cursor()
        print("Connected to SQLite")

        sqlite_create_table_query = '''CREATE TABLE directory
                                        (name text, date current_date , signature text, modifiedDate timestamp);'''
        c = connection.cursor()
        c.execute(sqlite_create_table_query)

        # insert directory detail
        sqlite_insert_with_param = """INSERT INTO 'directory'
                                        ('date', 'name', 'signature') 
                                        VALUES (?, ?, ?);"""

        data_tuple = (date, name, signature)
        c.execute(sqlite_insert_with_param, data_tuple)
        connection.commit()
        print("Directory added successfully \n")

        # get developer detail
        sqlite_select_query = """SELECT name, date, signature from directory where name = ?"""

        c.execute(sqlite_select_query, (1,))
        records = c.fetchall()

        for row in records:
            directory = row[0]
            date = row[1]
            signature = row[2]
            print("The directory: ", directory, " was added on ", date)
            print("The signature is: ", signature)

        c.close()

    except sqlite3.Error as error:
        print("Error while processing with SQLite", error)
    finally:
        if (connection):
            connection.close()
            print("SQLite connection is closed")


addDirectory(datetime.datetime.now(), "YYYYRRRRMMMMM", "FDKJFDHJGBFDGFDG546546546825D4F5S6")

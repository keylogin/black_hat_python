#!/usr/bin/python3
import sqlite3
import mariadb
from mysql.connector import Error

class MySQLiteConnection:
    def __init__(self):
        try:
            self.db = sqlite3.connect('testdb.db')
            self.db.commit()
            print("Connect to SqLite3")
        except sqlite3.Error as e:
            print(e)

    def close(self):
        if self.db:
            self.db.close()


class MyMySQLConnection:
    def __init__(self):
        try:
            self.connection = mariadb.connect(host='localhost', database="testdb", user="root", password="pass")
            if self.connection:
                print("Connected to MySQL from 'connection' object")
        except mariadb.Error as e:
            print(e)

    def close(self):
        if self.connection:
            self.connection.close()


def main():
    try:
        ConnectToMySQL = MyMySQLConnection()
        ConnectToSQLite = MySQLiteConnection()
    except Exception as e:
        print(e)
    finally:
        if 'ConnectToMySQL' in locals():
            ConnectToMySQL.close()
        if 'ConnectToSQLite' in locals():
            ConnectToSQLite.close()


if __name__ == "__main__":
    main()
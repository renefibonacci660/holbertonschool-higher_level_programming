#!/usr/bin/python3
'''
    Lists all states from given database
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    '''
        cursor.execute = executing the SQL query
        cursor.execute = fetching all the results
    '''
    connection = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'"
                   "ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for eachRow in rows:
        print(eachRow)

    cursor.close()
    connection.close()

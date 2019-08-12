#!/usr/bin/python3
'''
    Lists all cities of a state from given database
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    '''
        cursor.execute = executing the SQL query
        cursor.execute = fetching all the results
        using with so it closes by default instead of specifying ourselves
    '''

    with MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                         user=argv[1], passwd=argv[2], db=argv[3]) as database:

        chosen = ("SELECT cities.name FROM cities LEFT JOIN states"
                  " ON cities.state_id = states.id"
                  " WHERE states.name = %s"
                  " ORDER BY cities.id ASC")

        database.execute(chosen, [argv[4]])
        table = database.fetchall()
        print(", ".join([data[0] for data in table]))

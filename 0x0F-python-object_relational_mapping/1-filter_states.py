#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Retrieve arguments
    username, password, database = argv[1], argv[2], argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    # Create a cursor to execute queries
    cur = db.cursor()

    # Execute SQL query to select states with names starting with 'N'
    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
            )

    # Fetch and print results
    results = cur.fetchall()
    for row in results:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()

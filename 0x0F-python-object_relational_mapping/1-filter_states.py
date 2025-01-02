#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor to interact with the database
    cursor = db.cursor()

    # Execute SQL query to select states with names starting with 'N'
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
            )

    # Fetch and print all rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()

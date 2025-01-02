#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments: mysql username, password, database name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute query to get cities with theirstate names,sorted by cities.id
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Fetch all results and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()

#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get the arguments
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
    cursor = db.cursor()

    # Query to select all cities with their corresponding state names
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Fetch and display the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

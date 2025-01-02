#!/usr/bin/python3
import MySQLdb
import sys


def main():
    # Check if the correct number of arguments are passed
    if len(sys.argv) != 4:
        print(
                "Usage: ./4-cities_by_state.py "
                "<mysql_username> <mysql_password> <database_name>")
        return

    # Get the command-line arguments
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            user=mysql_user,
            passwd=mysql_pass,
            db=db_name
            )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Query to select all cities and their matchindg state names, by cities.id
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Fetch all the results
    rows = cursor.fetchall()

    # Print the results as specified
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

#!/usr/bin/python3
import MySQLdb
import sys


def list_cities(username, password, database):
    """
    Lists all cities from the database,
    ordered by cities.id in ascending order.

    Arguments:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
    """
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


if __name__ == "__main__":
    # Ensure the script is executed with the required arguments
    if len(sys.argv) != 4:
        print(
                "Usage: ./4-cities_by_state.py "
                "<mysql_username> <mysql_password> <database_name>"
                )
        sys.exit(1)

    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Call the function to list the cities
    list_cities(mysql_username, mysql_password, database_name)

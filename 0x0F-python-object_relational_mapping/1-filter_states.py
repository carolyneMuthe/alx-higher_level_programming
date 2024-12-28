#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    # Create a cursor to execute queries
    cur = db.cursor()
    
    # Execute SQL query to find states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    
    # Fetch all results
    rows = cur.fetchall()
    
    # Print each row
    for row in rows:
        print(row)
    
    # Close the cursor and the database connection
    cur.close()
    db.close()

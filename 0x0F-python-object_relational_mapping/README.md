# Python - Object-Relational Mapping

## Overview
This project demonstrates how to interact with a MySQL database using:
1. **MySQLdb**: A Python module for direct SQL queries.
2. **SQLAlchemy**: A Python ORM for abstracting database interactions.

## Files
- `fetch_states.py`: Fetches and lists all states from a MySQL database using MySQLdb.
- `model_state.py`: Defines the `State` model for SQLAlchemy ORM.
- `fetch_states_orm.py`: Fetches and lists all states from a MySQL database using SQLAlchemy ORM.

## Usage
Run each script with the following syntax:
```bash
./<script_name>.py <mysql_username> <mysql_password> <database_name>


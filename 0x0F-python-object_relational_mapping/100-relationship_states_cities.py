#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
import sys
import mysql.connector

def fetch_cities_by_state(db_user, db_password, db_name):
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user=db_user,
            password=db_password,
            database=db_name
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Query to fetch cities grouped by states
            query = """
                    SELECT s.name AS state_name, c.id, c.name AS city_name
                    FROM states s
                    JOIN cities c ON s.id = c.state_id
                    ORDER BY s.name, c.name
                    """
            cursor.execute(query)

            # Fetch all rows
            cities = cursor.fetchall()

            # Initialize state variable to track state changes
            current_state = None

            # Iterate through results and print in the specified format
            for state_name, city_id, city_name in cities:
                if state_name != current_state:
                    print(f"{state_name}:")
                    current_state = state_name
                print(f"  ({city_id}) {city_name}")

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        # Close database connection
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 14-model_city_fetch_by_state.py <db_user> <db_password> <db_name>")
        sys.exit(1)

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    fetch_cities_by_state(db_user, db_password, db_name)

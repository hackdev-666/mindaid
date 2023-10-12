import mysql.connector
import hashlib

# Function to register a user
def register_user(username, age, email, phone_number, gender, password):
    try:
        connection = mysql.connector.connect(
            host='your_host',
            user='your_user',
            password='your_password',
            database='mydb'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Hash the password
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            # Insert user data into the "users" table
            insert_query = "INSERT INTO users (username, age, email, phone_number, gender, password_hash) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (username, age, email, phone_number, gender, password_hash))
            connection.commit()
            print("Registration successful")

    except mysql.connector.Error as e:
        print(f"Error registering user: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to log in a user
def login_user(phone_number, password):
    try:
        connection = mysql.connector.connect(
            host='your_host',
            user='your_user',
            password='your_password',
            database='mydb'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Hash the provided password
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            # Check if login credentials are valid
            select_query = "SELECT * FROM users WHERE phone_number = %s AND password_hash = %s"
            cursor.execute(select_query, (phone_number, password_hash))
            user = cursor.fetchone()

            if user:
                print("Login successful")
                print(f"Welcome, {user[1]}")
            else:
                print("Login failed")

    except mysql.connector.Error as e:
        print(f"Error logging in: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

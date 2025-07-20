# login_system.py

# Predefined user credentials
users = {
    "admin": "admin123",
    "user1": "password1",
    "user2": "securepass"
}

# Login Function
def login():
    print("=== LOGIN SYSTEM ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid credentials. Access denied.")

# Run the login
login()
# Program to validate username and password

username = input("Enter username: ")
password = input("Enter password: ")

# Assuming correct username and password
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")
#output
"""Enter username: admin
Enter password: 1234
Login Successful"""
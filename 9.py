def login_system():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "admin123":
        print("Admin Access")
    elif username == "user" and password == "user123":
        print("Limited Access")
    elif username == "guest" and password == "":
        print("Minimal Access")
    else:
        print("Access Denied")

from auth_db import authenticate, create_user, user_exists

logged_in = None

while True:
    action = input("Type login / exit: ").lower()

    if action == "exit":
        break

    if action == "login":
        username = input("Username: ")
        password = input("Password: ")

        if authenticate(username, password):
            logged_in = username
            print("you are now logged in")
        else:
            print("User not found or wrong password")
            signup = input("Do you want to sign up? (yes/no): ").lower()

            if signup == "yes":
                while True:
                    new_username = input("Choose username: ")
                    if not user_exists(new_username):
                        break
                    print("Username already exists")

                new_password = input("Choose password: ")
                create_user(new_username, new_password)
                print("User registered successfully")

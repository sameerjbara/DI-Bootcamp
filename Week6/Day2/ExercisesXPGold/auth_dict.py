users = {
    "alice": "1234",
    "bob": "abcd",
    "charlie": "pass"
}

logged_in = None

while True:
    action = input("Type login / exit: ").lower()

    if action == "exit":
        break

    if action == "login":
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username] == password:
            logged_in = username
            print("you are now logged in")
        else:
            print("User not found")
            signup = input("Do you want to sign up? (yes/no): ").lower()

            if signup == "yes":
                while True:
                    new_username = input("Choose username: ")
                    if new_username not in users:
                        break
                    print("Username already exists")

                new_password = input("Choose password: ")
                users[new_username] = new_password
                print("User registered successfully")

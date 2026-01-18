# Exercise 1: Bank Account
# Instructions
# Part I:

# Create a class called BankAccount that contains the following attributes and methods:
# balance - (an attribute)
# __init__ : initialize the attribute
# deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
# withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive


# Part II : Minimum balance account

# Create a MinimumBalanceAccount that inherits from BankAccount.
# Extend the __init__ method and accept a parameter called minimum_balance with a default value of 0.
# Override the withdraw method so it only allows the user to withdraw money if the balance remains higher than the minimum_balance, raise an Exception if not.


# Part III: Expand the bank account class

# Add the following attributes to the BankAccount class:
# username
# password
# authenticated (False by default)

# Create a method called authenticate. This method should accept 2 strings : a username and a password. If the username and password match the attributes username and password the method should set the authenticated boolean to True.

# Edit withdraw and deposit to only work if authenticated is set to True, if someone tries an action without being authenticated raise an Exception


# Part IV: BONUS Create an ATM class

# __init__:
# Accepts the following parameters: account_list and try_limit.

# Validates that account_list contains a list of BankAccount or MinimumBalanceAccount instances.
# Hint: isinstance()

# Validates that try_limit is a positive number, if you get an invalid input raise an Exception, then move along and set try_limit to 2.
# Hint: Check out this tutorial

# Sets attribute current_tries = 0

# Call the method show_main_menu (see below)

# Methods:
# show_main_menu:
# This method will start a while loop to display a menu letting a user select:
# Log in : Will ask for the users username and password and call the log_in method with the username and password (see below).
# Exit.

# log_in:
# Accepts a username and a password.

# Checks the username and the password against all accounts in account_list.
# If there is a match (ie. use the authenticate method), call the method show_account_menu.
# If there is no match with any existing accounts, increment the current tries by 1. Continue asking the user for a username and a password, until the limit is reached (ie. try_limit attribute). Once reached display a message saying they reached max tries and shutdown the program.

# show_account_menu:
# Accepts an instance of BankAccount or MinimumBalanceAccount.
# The method will start a loop giving the user the option to deposit, withdraw or exit.
class BankAccount:
    def __init__(self, balance=0, username="", password=""):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
            return True
        self.authenticated = False
        return False

    def _check_authenticated(self):
        if not self.authenticated:
            raise Exception("Action not allowed: please log in first.")

    def deposit(self, amount):
        self._check_authenticated()
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Deposit amount must be a positive int.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self._check_authenticated()
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Withdraw amount must be a positive int.")
        self.balance -= amount
        return self.balance


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, username="", password="", minimum_balance=0):
        super().__init__(balance=balance, username=username, password=password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        self._check_authenticated()
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Withdraw amount must be a positive int.")
        if self.balance - amount < self.minimum_balance:
            raise Exception("Cannot withdraw: balance would go below minimum balance.")
        self.balance -= amount
        return self.balance


class ATM:
    def __init__(self, account_list, try_limit):
        # Validate account_list
        if not isinstance(account_list, list) or not all(
            isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list
        ):
            raise Exception("account_list must be a list of BankAccount/MinimumBalanceAccount instances.")

        self.account_list = account_list

        # Validate try_limit
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("Invalid try_limit given, setting try_limit to 2.")
            self.try_limit = 2
        else:
            self.try_limit = try_limit

        self.current_tries = 0

        # Start ATM
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n===== ATM Main Menu =====")
            print("1) Log in")
            print("2) Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                self.log_in(username, password)
            elif choice == "2":
                print("Goodbye 👋")
                break
            else:
                print("Invalid choice, try again.")

    def log_in(self, username, password):
        while self.current_tries < self.try_limit:
            for account in self.account_list:
                if account.authenticate(username, password):
                    print(f"✅ Logged in as {account.username}")
                    self.current_tries = 0
                    self.show_account_menu(account)
                    return

            self.current_tries += 1
            if self.current_tries >= self.try_limit:
                print("Max tries reached. Shutting down.")
                raise SystemExit

            print(f"Wrong credentials. Attempts left: {self.try_limit - self.current_tries}")
            username = input("Username: ").strip()
            password = input("Password: ").strip()

    def show_account_menu(self, account):
        while True:
            print("\n===== Account Menu =====")
            print(f"Balance: {account.balance}")
            print("1) Deposit")
            print("2) Withdraw")
            print("3) Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                try:
                    amount = int(input("Deposit amount (positive int): ").strip())
                    new_balance = account.deposit(amount)
                    print(f"Deposited. New balance: {new_balance}")
                except Exception as e:
                    print(e)

            elif choice == "2":
                try:
                    amount = int(input("Withdraw amount (positive int): ").strip())
                    new_balance = account.withdraw(amount)
                    print(f"Withdrawn. New balance: {new_balance}")
                except Exception as e:
                    print(e)

            elif choice == "3":
                print("Logging out...")
                account.authenticated = False
                break
            else:
                print("Invalid choice, try again.")


# -------------------- TEST / DEMO --------------------
if __name__ == "__main__":
    acc1 = BankAccount(balance=1000, username="sara", password="1234")
    acc2 = MinimumBalanceAccount(balance=500, username="john", password="abcd", minimum_balance=200)

    ATM([acc1, acc2], try_limit=3)

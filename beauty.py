'''
Dangote is happy with your help so far, but he would like to make some changes.
He would like to introduce saving accounts and current accounts.
If you deposit money in a current account and the money stays for one month, you get an interest of 1%, but if you have a savings account, the interest is 3% and you can only withdraw after 6 months.
'''
from datetime import datetime
from datetime import timedelta


# Client class(Parent Class) taking the parenthesis/attributes name, age and contact of the user
class Client:
    # name = input("Please, Enter your name:\n")
    # age = input("How old are you?\n")
    # contact = input("What is your contact address?\n")
    print("Hello,\nWelcome to Dangote Bank")
    deposit = 0

    def __init__(self, name, age, contact, ):
        self.name = name
        self.age = age
        self.contact = contact


# Bank class(child class) inhereted the parentheses/attributes of client class
class Bank(Client):
    withdraw = 0
    balance = 0

    def __init__(self, name, age, contact, balance, account_type, deposit_day, withdraw_day, tr_day):
        super().__init__(name, age, contact)
        self.balance = balance
        self.account_type = account_type
        self.deposit_day = deposit_day
        self.withdraw_day = withdraw_day
        self.tr_day = tr_day

    # method/function(register), this accept input from user and store it as the client's registration information
    def register(self):
        registered_name = input("Please enter your full name")
        self.name = registered_name
        registered_age = int(input("Please enter your age"))
        self.age = registered_age
        registered_address = input("Please enter your address")
        self.contact = registered_address
        account_type = input(
            "What type of account do you want to create?\nEnter 1 Current account or 2 savings account\n")
        self.account_type = account_type
        if account_type == '1':
            self.account_type = "Current account"
        elif account_type == '2':
            self.account_type = "Savings account"
        else:
            print("Input a valid option")
            welcome_note(Client)
        print(f"Thank you", registered_name, "for opening an account with us\nYour info are as follows:\nName",
              registered_name, "\nAge:", registered_age, "\nContact info:", registered_address, "\nAccount type: ",
              self.account_type)
        action = input("Would you like to perform a transaction?, Type 1 for yes and 0 for no\n")
        if action == '1':
            welcome_note(Client)
        elif action == '0':
            exit()
        else:
            print("Please, input correct option")

    # method/function(details), this accept info from registration function and prints the user's bank details
    # balance is placed at zero because people registers their account without money
    def details(self):
        print(f"Dear {self.name},\nYour account details is as follow:\nName:{self.name}\nAge:{self.age}\nContact:{self.contact}\nAccount balance: {self.balance}\nThank you for Banking with us ")
        action = input("Would you like to perform a transaction?, Type 1 for yes and 0 for no\n")
        if action == '1':
            welcome_note(Client)
        else:
            exit()

    # method/function(deposit), this function ask for an input which will then be stored
    # balance will keep increasing by the specific amount deposited
    def deposit(self):
        depositing = float(input(f"Hello{self.name}, How much do you want to deposit?"))
        self.balance += depositing
        deposit_day = datetime.today()
        self.deposit_day = deposit_day
        print(f"You have credited your account with RWF{depositing}.\nThank you for banking with us."
              f"Balance: RWF{self.balance}")
        action = input("Would you like to perform a transaction?, Type 1 for yes and 0 for no\n")
        if action == '1':
            welcome_note(Client)
        else:
            exit()

    # method/function(withdraw), this function ask for an input which will then be stored if the amount to withdraw
    # is greater than the balance, and error is printed out and the user is prompt to input correct amount balance
    # will keep decreasing by the specific amount withdraw
    def withdraw(self):
        withdrawal = float(input(f'Hello{self.name}, How much do you want to withdraw?'))
        if self.balance < withdrawal:
            print("Insufficient Fund")
        else:
            withdraw_day = datetime.today()
            interest_Currentaccount = (self.deposit_day + timedelta(days=30))
            interest_savingsaccount = (self.deposit_day + timedelta(days=180))
            print(f"You have debited your account with RWF{withdrawal}.\nThank you for banking with us.")
            if self.account_type == "Current account" and withdraw_day == interest_Currentaccount:
                self.balance = self.balance + (self.balance * 0.01)
            elif self.account_type == "Savings account" and withdraw_day == interest_savingsaccount:
                self.balance = self.balance + (self.balance * 0.03)
            else:
                print("You are not entitled to interest this time because of your withdrawl")
            self.balance -= withdrawal
            print(f"Balance: RWF{self.balance}")
        action = input("Would you like to perform a transaction?, Type 1 for yes and 0 for no\n")
        if action == '1':
            welcome_note(Client)
        else:
            exit()

    # method/function(transferring), this function ask for an input which will then be stored
    # if the amount to transfer is greater than the balance, and error is printed out and the user is prompt to input correct amount
    # balance will keep decreasing by the specific amount transfer
    def transfer(self):
        transferring = float(input(f'Hello {self.name}, How much do you want to transfer?'))
        tr_account = int(input("Enter the account number you want to transfer to:\n"))
        if self.balance < transferring:
            return "Insufficient Fund"
        else:
            tr_day = datetime.today()
            interest_Currentaccount = self.deposit_day + timedelta(days=30)
            interest_savingsaccount = self.deposit_day + timedelta(days=180)
            print(f"You have debited your account with RWF{transferring}\nYou have transfered to{tr_account}\nThank you for banking with us.")
            if self.account_type == "Current account" and tr_day == interest_Currentaccount:
                self.balance = self.balance + (self.balance * 0.01)
            elif self.account_type == "Savings account" and tr_day == interest_savingsaccount:
                self.balance = self.balance + (self.balance * 0.03)
            else:
                print("You are not entitled to interest this time because of your withdrawl")
            self.balance -= transferring
            print(f"Balance RWF{self.balance}")
            action = input("Would you like to perform a transaction? Type 1 for yes and 0 for no\n")
            if action == '1':
                welcome_note(Client)
            else:
                exit()


# This method is defined so as to give the user the option
def welcome_note(Client):
    print("\nThank you for choosing Dangote Bank!")
    option = input(
        "What would you like to do?Press\n1)To open an account with us.\n2)Check your account balance\n3)Withdraw\n4)Transfer\n5)Deposit\n6)Quit\n")
    if option == '1':
        Bank.register(Bank)
    elif option == '2':
        Bank.details(Bank)
    elif option == '3':
        Bank.withdraw(Bank)
    elif option == '4':
        Bank.transfer(Bank)
    elif option == '5':
        Bank.deposit(Bank)
    elif option == '6':
        exit()
    else:
        print("Please Enter the correct option")
        welcome_note(Client)


welcome_note(Client)


import random

class BankAccount:

#constructor to show account name, number, and amount of money 
    def __init__(self,account_name):
        self.account_name = account_name 
        self.account_amount = 0
        self.account_number = random.randint(10000,99999)

#method to verify deposit amount is > 0 and add it to account
    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.account_amount = self.account_amount + deposit_amount
        else:
            print("Error, deposit amount needs to be > $0.")

#method to confirm withdrawal amount is less than amount in account then subtracting it from account
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.account_amount:
            print("Error, can not withdraw amount > balance.")
        else:
            self.account_amount = self.account_amount - withdraw_amount

#method displays user account info
    def view(self):
        print(f"Name:{self.account_name}")
        print(f"Balance:${self.account_amount:.2f}")
        print(f"Account Number {self.account_number}")
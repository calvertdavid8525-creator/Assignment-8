#intro
from Assignment_8.Assignment_8_Functions import BankAccount
print("Welcome to the Bank of David")
customer_name = input("Please enter your name: ")

user_choice = 0
bank_account = BankAccount(customer_name)

#display choices for user
while user_choice !=4:
    print()
    print("1. Make a deposit")
    print("2. Make a withdrawl")
    print("3. View account information")
    quit = print("4. Quit")
    print()

    user_choice = int(input("Please choose an option: "))
    print()

#user deposit
    if user_choice == 1:
        print("Deposit selected.")
        user_deposit = float(input("Enter deposit amount: "))
        bank_account.deposit(user_deposit)

#user withdrawal
    elif user_choice == 2:
        print("Withdrawal selected.")
        user_withdraw = float(input("Enter withdrawal amount: "))
        bank_account.withdraw(user_withdraw)

#user displays account info
    elif user_choice == 3:
        print("View account information selected.")
        bank_account.view()

#Exit
    elif user_choice == 4:
        print("Thank you! Have a great day!")
    else:
        print("Please choose an option 1-4: ")

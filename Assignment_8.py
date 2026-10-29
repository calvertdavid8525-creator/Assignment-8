# Use at least two files.
# • Use one function for each of the first three options.
# • Use meaningful variable and method names.
# • Format monetary amounts as dollar values with two decimal places.
# • Make sure deposits and withdrawals change the account balance correctly.
# • Test your program with several deposits, withdrawals, invalid choices, and attempted
# withdrawals that exceed the account balance.
# • Your output does not need to match the sample session exactly, but it should provide
# equivalent information.
from Assignment_8.Assignment_8_Functions import BankAccount
print("Welcome to the Bank of David")
customer_name = input("Please enter your name: ")

user_choice = 0
bank_account = BankAccount(customer_name)

while user_choice !=4:
    print()
    print("1. Make a deposit")
    print("2. Make a withdrawl")
    print("3. View account information")
    quit = print("4. Quit")
    print()

    user_choice = int(input("Please choose an option: "))
    print()
    if user_choice == 1:
        print("Deposit selected.")
        user_deposit = float(input("Enter deposit amount: "))
        bank_account.deposit(user_deposit)
    
    elif user_choice == 2:
        print("Withdrawal selected.")
        user_withdraw = float(input("Enter withdrawal amount: "))
        bank_account.withdraw(user_withdraw)

    elif user_choice == 3:
        print("View account information selected.")
        bank_account.view()

    elif user_choice == 4:
        print("Thank you! Have a great day!")
    else:
        print("Please choose an option 1-4: ")

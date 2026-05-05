# Program name: Transaction Tracker CLI
# Programmer: Jessie Conn
# Description: Simulates a simple bank account with deposits and withdrawals,
# preventing overdrafts and allowing repeated transactions.
# Inspired by a practice program prompt in chapter 4 of "Automate the Boring Stuff Workbook",
# by Al Swigert. 

def after_transaction(balance, transaction):
    if balance + transaction < 0:
        print("Transaction denied: insufficient funds.")
        return balance
    else:
        return balance + transaction


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


def main():
    print("=== Welcome to Simple Bank ===\n")

    balance = get_integer("Enter your starting balance: ")

    while True:
        print(f"\nCurrent balance: ${balance}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = get_integer("Enter deposit amount: ")
            balance = after_transaction(balance, amount)

        elif choice == "2":
            amount = get_integer("Enter withdrawal amount: ")
            balance = after_transaction(balance, -amount)

        elif choice == "3":
            print("\nGoodbye. Try not to spend it all in one place.")
            break

        else:
            print("Invalid choice. Try again.")


# Run the program
main()

class BankAccount:
    def __init__(self, account_number, name, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} deposited.")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount {amount} withdrawn.")
        else:
            print("Insufficient balance.")
    
    def display_balance(self):
        print(f"Current balance: {self.balance}")
        
# main program
print("Welcome to the Bank!\n")

accounts = []

while True:
    print("What would you like to do?")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Quit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        account_number = input("Enter account number: ")
        name = input("Enter name: ")
        initial_balance = float(input("Enter initial balance: "))
        account = BankAccount(account_number, name, initial_balance)
        accounts.append(account)
        print("Account created.")
    elif choice == "2":
        account_number = input("Enter account number: ")
        for account in accounts:
            if account.account_number == account_number:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
                break
        else:
            print("Account not found.")
    elif choice == "3":
        account_number = input("Enter account number: ")
        for account in accounts:
            if account.account_number == account_number:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
                break
        else:
            print("Account not found.")
    elif choice == "4":
        account_number = input("Enter account number: ")
        for account in accounts:
            if account.account_number == account_number:
                account.display_balance()
                break
        else:
            print("Account not found.")
    elif choice == "5":
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice. Please try again.\n")

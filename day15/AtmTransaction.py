class InsufficientBalanceError(Exception):
    """Custom exception for insufficient balance."""
    pass


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.balance += amount
            print(f"₹{amount} deposited successfully. Current balance: ₹{self.balance}")
        except ValueError as e:
            print("Error:", e)

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance for this withdrawal.")
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}")
        except (ValueError, InsufficientBalanceError) as e:
            print("Error:", e)

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")


# Testing the ATM system
account = BankAccount(5000)  # Starting balance ₹5000

while True:
    print("\n🏦 ATM Menu: 1. Check Balance | 2. Deposit | 3. Withdraw | 4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            account.check_balance()

        elif choice == 2:
            amount = float(input("Enter deposit amount: ₹"))
            account.deposit(amount)

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: ₹"))
            account.withdraw(amount)

        elif choice == 4:
            print("Thank you for using our ATM! 😊")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

    except ValueError:
        print("Invalid input! Please enter a number.")

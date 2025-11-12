class ATM:
    def __init__(self,balance=0):
        self.__balance = balance
        
        
    def check_balance(self):
            print(f"Your balance is : ${self.__balance}")
            
    def deposit(self,amount):
            if amount>0:
                self.__balance += amount
                print(f"${amount} deposited successfully!")
            else:
                print("Deposit amount must be positive.")
                
    def withdraw(self, amount):
            if 0 < amount <= self.__balance:
                 self.__balance -= amount
                 print(f"${amount} withdrawn successfully!")
            else:
                 print("Insufficient balance or invalid amount.")
        
        
        
user1 = ATM(1000)        # Starting balance = $1000

user1.check_balance()    # Check initial balance
user1.deposit(500)       # Deposit $500
user1.check_balance()    # Check balance after deposit
user1.withdraw(300)      # Withdraw $300
user1.check_balance()    # Check balance after withdrawal
user1.withdraw(1500) 
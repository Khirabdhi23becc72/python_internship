class BankAccount:
    def _init_(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount:.2f} into account {self.account_number}.")
        else:
            print("Deposit amount must be greater than zero.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount:.2f} from account {self.account_number}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdraw amount must be greater than zero.")
    
    def get_balance(self):
        return self.balance

# Example usage:
if __name__ == "_main_":
    account1 = BankAccount("123456789", "Alice Brown", 1000.0)
    
    print(f"Current balance of account {account1.account_number}: ₹{account1.get_balance():.2f}")
    
    account1.deposit(500.0)
    print(f"Current balance after deposit: ₹{account1.get_balance():.2f}")
    
    account1.withdraw(200.0)
    print(f"Current balance after withdrawal: ₹{account1.get_balance():.2f}")
    
    account1.withdraw(1500.0)  # Attempting to withdraw more than balance
    print(f"Current balance after attempted withdrawal: ₹{account1.get_balance():.2f}")
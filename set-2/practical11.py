class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit_or_withdraw(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        elif amount < 0:
            withdrawal = abs(amount)
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f"Withdrew: {withdrawal}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount.")
    
    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return 'Invalid deposit amount'
        else:
            self.balance += amount
            return f'Deposit of R${amount} done. Your new balance is {self.balance}'
    
    def withdraw(self, amount):
       if amount > self.balance:
           return 'Insufficiente funds for withdrawal'
       elif amount <= 0:
           return 'Invalid withdraw amount'
       else:
           self.balance -= amount
           return f'Withdraw of R${amount} done. Your new balance is {self.balance}'
       
    def transfer(self, other_account, amount):
        if amount <= 0:
            return 'Invalid transfer amount'
        
        if amount > self.balance:
            return 'Insuficient funds'

        self.balance -= amount
        other_account.balance += amount

        return f"Transfer of R${amount} from {self.owner} to {other_account.owner} completed"


       
    def show_balance(self):
        return f'Hello, {self.owner}! Your balance is {self.balance}'
    




account1 = BankAccount("Luis")
account2 = BankAccount("Laura")

print(account1.deposit(1500))
print(account2.deposit(15))

print(account1.transfer(account2, 1200))
print(account1.show_balance())
print(account2.show_balance())


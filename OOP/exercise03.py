class BankAccount():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, value):

        if value <= 0:
            return "Valor depósito inválido. Deposite um valor positivo!"
        else:
            self.balance += value

    
    def withdraw(self, value):

        if value > self.balance or value <= 0:
            return "Valor saque inválido. Saque um valor disponivel no seu saldo!"
        else:
            self.balance -= value

    def __str__(self):
        return f"Sr. {self.owner} seu saldo é de {self.balance}"
    

minha_conta = BankAccount("Luis Guilherme")
minha_conta.deposit(100)
print(minha_conta)

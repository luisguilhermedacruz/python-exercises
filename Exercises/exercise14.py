class ValorInvalidoError(Exception):
    pass


class SaldoInsuficienteError(Exception):
    pass


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("O valor para depósito deve ser maior que zero.")

        self.saldo += valor
        return f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}"

    def sacar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("O valor para saque deve ser maior que zero.")

        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")

        self.saldo -= valor
        return f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}"

    def mostrar_saldo(self):
        return f"Titular: {self.titular} | Saldo: R${self.saldo}"


conta = ContaBancaria("Luis", 100)

try:
    print(conta.depositar(50))
    print(conta.sacar(30))
    print(conta.mostrar_saldo())

    print(conta.sacar(500)) 
except ValorInvalidoError as erro:
    print(f"Erro de valor: {erro}")
except SaldoInsuficienteError as erro:
    print(f"Erro de saldo: {erro}")





    
        
valor_para_depositar = int(input("Quanto em R$ você quer depósitar? "))
valor_para_sacar = int(input("Quanto em R$ você quer sacar? "))


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor_para_depositar):
        if valor_para_depositar <= 0:
            return "O valor que você deseja depósitar é inválido!"

        self.saldo += valor_para_depositar

        with open("demonstrativo.txt", "a", encoding="utf-8") as demonstrativo:
            demonstrativo.write(
                f"Depósito de R${valor_para_depositar} na conta de {self.titular}\n"
            )

        return f"Depósito realizado com sucesso. Saldo atual: R${self.saldo}"

    def sacar(self, valor_para_sacar):
        if valor_para_sacar > self.saldo or valor_para_sacar <= 0:
            return "O valor que você deseja sacar não é permitido. Consulte seu gerente."

        self.saldo -= valor_para_sacar

        with open("demonstrativo.txt", "a", encoding="utf-8") as demonstrativo:
            demonstrativo.write(
                f"Saque de R${valor_para_sacar} na conta de {self.titular}\n"
            )

        return f"Saque realizado com sucesso. Saldo atual: R${self.saldo}"

    def mostrar_saldo(self):
        return f"Seu saldo é: R${self.saldo}"

    def mostrar_demonstrativo(self):
        with open("demonstrativo.txt", "r", encoding="utf-8") as demonstrativo:
            return demonstrativo.read()


conta = ContaBancaria("Luis")

print(conta.depositar(valor_para_depositar))
print(conta.sacar(valor_para_sacar))
print(conta.mostrar_saldo())
print(conta.mostrar_demonstrativo())






    
        
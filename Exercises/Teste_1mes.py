# =========================
# Python Fundamentals Test
# =========================

# -------- Question 1 --------
def verification_number(number: int) -> str:
    if number > 0:
        return f"The {number} is positive!"
    elif number < 0:
        return f"The {number} is negative!"
    else:
        return "Your number is zero!"


# -------- Question 2 --------
for i in range(1, 11):
    print(i)

for p in range(1, 11):
    if p % 2 == 0:
        print(p)


# -------- Question 3 --------
def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"

print(saudacao("Luis"))


# -------- Question 4 --------
numbers = [10, 20, 30, 40, 50]

def sum_one(numbers: list[int]) -> str:
    return f"The sum of all numbers is {sum(numbers)}"

def sum_two(numbers: list[int]) -> str:
    sum_all = 0
    for p in numbers:
        sum_all += p
    return f"The sum of all numbers is {sum_all}"

print(numbers[0])
print(numbers[-1])
print(sum_one(numbers))
print(sum_two(numbers))


# -------- Question 5 --------
notas = [7, 8, 5, 10, 6]

def avalia_aluno(notas: list[int]) -> str:
    media = sum(notas) / len(notas)

    if media >= 7:
        return "Aluno aprovado!"
    else:
        return "Aluno reprovado!"

print(avalia_aluno(notas))


# -------- Question 6 --------
# Esse código recebe dois valores como parâmetro de uma função,
# retorna a multiplicação deles, armazena em uma variável e imprime o resultado.


# -------- Question 7 --------
# O erro lógico é que deveria usar >= 18, pois 18 já é maior de idade.


# -------- Question 8 --------
# Serve para executar código apenas quando o arquivo é rodado diretamente,
# e não quando ele é importado como módulo.


# -------- Question 9 --------
# 1 - Classe é o molde
# 2 - __init__ inicializa o objeto
# 3 - self representa o próprio objeto
# 4 - Exemplo de instância: carro1 = Carro("ONIX")


# -------- Question 10 --------
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor} realizado. Novo saldo: {self.saldo}"


conta1 = ContaBancaria("Luis")
print(conta1.depositar(100))
print(f"{conta1.titular}, saldo: {conta1.saldo}")


# -------- Question 11 --------
# Pensamento: criar uma entidade transação com:
# tipo (entrada/saida), valor, data, user_id
# e funções para cálculo de lucro, etc.


# -------- Question 12 --------
numbers = [4, 9, 2, 15, 7]

def verification_biggest(numbers: list[int]) -> int:
    big_number = numbers[0]
    for b in numbers:
        if b > big_number:
            big_number = b
    return big_number

print(verification_biggest(numbers))
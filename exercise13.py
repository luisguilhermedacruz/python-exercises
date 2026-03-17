def saudacao(nome: str) -> str:
    return f'Olá, {nome}'

def despedida(nome: str) -> str:
    return f'Até mais {nome}'


if __name__ == "__main__":
    print("Testando módulo...")
    print(saudacao("Luis"))
    print(despedida("Luis"))
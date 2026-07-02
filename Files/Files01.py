with open("notas.txt", "w") as arquivo:
    arquivo.write("NOME: LUIS GUILHERME" " NOTA: 10\n")
    arquivo.write("NOME: LAURA CRUZ" " NOTA: 10\n")
    arquivo.write("NOME: SANDRA" " NOTA: 10\n")
    arquivo.write("NOME: ANTONIO" " NOTA: 10\n")
    arquivo.write("NOME: GLORIA" " NOTA: 10\n")

with open("notas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())

with open("notas.txt", "a") as arquivo:
    arquivo.write("NOME: ULTIMO ALUNO " "NOTA: 10 ")

with open("notas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha)

with open("notas.txt", "r") as arquivo:
    content = arquivo.read()
    print(content)
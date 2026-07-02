with open("corridas.txt", "w") as valores:
    valores.write("DATE: 01/07/2027" "UBER: R$100,00" "99: R$100,00" "INDRIVER: R$90 \n")
with open("corridas.txt", "w") as valores:
    valores.write("DATE: 02/07/2027" "UBER: R$100,00" "99: R$100,00" "INDRIVER: R$90 \n")
with open("corridas.txt", "w") as valores:
    valores.write("DATE: 03/07/2027" "UBER: R$100,00" "99: R$100,00" "INDRIVER: R$90 \n")

with open("corridas.txt", "r", encoding="utf-8") as valores:
    valores_lidos = valores.read()
    print(valores_lidos)

with open("corridas.txt", "a") as valores:
    valores.write("DATE: 04/07/2027" "SEM CORRIDAS")

with open("corridas.txt", "r") as valores:
   for dias in valores:
       print(dias)

print("a" "b")
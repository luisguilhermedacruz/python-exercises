name = "Luis Guilherme"
age = 31
height = 1.78
like_coffee = True

print(type(name))
print(type(age))
print(type(height))
print(type(like_coffee))

age_convert = float(age)
height_convert = int(height)

print(age_convert)
print(height_convert)
print(type(age_convert))
print(type(height_convert)) 


temp = 15

if temp < 15:
    print("COLD")
elif temp <= 25:
    print("OK")
else:
    print("HOT")

hour = 12

if hour < 11.59:
    print("Good Morning")
elif hour <= 17.59:
    print("Good afternoon")
else:
    print("Good Night")


for i in range (1,11):
    if i % 2 == 0:
        print(i)





##
def area_retangulo(largura, altura):
        perimetro = (largura + altura) * 2
        return perimetro

print(area_retangulo(10, 1.78))


def saudacao(nome, idioma="pt"):
    if idioma == "pt":
        return f"Olá, {nome}"
    elif idioma == "en":
        return f"Hello, {nome}"
    else:
        return f"Hola, {nome}"
    
print(saudacao("Luis", "en"))

## while

count = 0

while count <= 100:
    somador = count + count
    print(somador)
    count += 1

    
    

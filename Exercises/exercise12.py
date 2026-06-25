user = {
    "name": input("DIGITE SEU NOME: "),
    "age": int(input("DIGITE SUA IDADE: ")),
    "city": input("DIGITE SUA CIDADE: ")
}

def create_user():
        with open("text.txt", "a", encoding="utf-8") as fileUser:
                if user["age"] >= 18:
                        fileUser.write(f'O usuário {user["name"]} tem {user["age"]} e é maior de idade! Ele mora em {user["city"]} e foi registrado com sucesso na nossa base de maiores!')
                else:
                       fileUser.write(f'O usuário {user["name"]} tem {user["age"]} e é menor de idade! Ele mora em {user["city"]} e foi registrado com sucesso na nossa base de menores!') 

def read_users():
        with open("text.txt", "r", encoding="utf-8") as fileUser:
                content = fileUser.read()
                print(content)          
        

create_user()
read_users()
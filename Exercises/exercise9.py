users = {
    "name": input("DIGITE SEU NOME: "),
    "age": int(input("DIGITE SUA IDADE: ")),
    "city":input("DIGITE SUA CIDADE: ")
}

if users["age"] > 18:
        print(f'O usuário {users["name"]} tem {users["age"]} anos, é maior de idade e mora em {users["city"]}')
else:
        print("USUÁRIO MENOR DE IDADE!")
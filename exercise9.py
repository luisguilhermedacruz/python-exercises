user = {
    "name":"Luis Guilherme",
    "age":"31",
    "city":"São Paulo"
}

print(user["name"])
print(user.keys())
print(user.values())
user["profissão"] = "Uber driver!"
user["age"] == 31
for key, values in user.items():
    print(key, values)


users = [
    {"name": "Luis", "age": 31},
    {"name": "Ana", "age": 25},
    {"name": "Carlos", "age": 40}
]

ana = [u for u in users if u["name"] == "Ana"]
print(ana)

for u in users:
    if u["name"] == "Carlos":
        print(u["name"],"tem",str(u["age"]) + " de idade") 

for l in users:
    if l["name"] == "Luis":
        print(f'{l["name"]} tem {l["age"]} de idade!')
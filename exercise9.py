person = {
    "name": "Luis",
    "age": "30",
    "city": "São Paulo"
}

def get_age(person: dict) -> int:
    return person["age"]

print(get_age(person))
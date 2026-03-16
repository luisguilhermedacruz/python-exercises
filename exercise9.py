person = {
    "name": "Luis",
    "age": "30",
    "city": "São Paulo"
}

def get_age(person: dict) -> int:
    return person["age"], person["city"]


cars_honda = {
    "modelo":"civic",
    "age": "2026",
    "color": "white"

}

print(get_age(person))
print(f"My dream's car is {cars_honda["modelo"]} of age {cars_honda["age"]} and color {cars_honda["color"]}")
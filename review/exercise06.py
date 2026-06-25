## test

shopping = ["shirts", "cap", "glass", "perfume", "pants"]
print(shopping)

shopping.append("celphone")
shopping.remove(shopping[1])
print(shopping)

for item in shopping:
    print(item)

    ## dict

person = {
    "name":"Luis",
    "age":31,
    "city":"São Paulo",
    "profission":"Driver",
    "favorite_language":"Python"
}

def return_dates(person: dict) -> None:
    for key, value in person.items():
        print(f"{key}:{value}")

print(return_dates(person))
print(person.get("profission"))

days = ("SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY")
work_day = list(days[1:6])


print(days)
print(work_day)

work_day.remove(work_day[1])
print(work_day)
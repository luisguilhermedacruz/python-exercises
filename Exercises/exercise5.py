numbers = [0,13,6,7,34,678,1000]

def filter_evenNumbers(list: list[int]) -> list[int]:
    even_numbers = []

    for e in list:
        if e % 2 == 0:
            even_numbers.append(e)

    return even_numbers

print(filter_evenNumbers(numbers))
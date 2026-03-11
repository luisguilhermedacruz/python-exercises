numbers = [10,20,50,766,23,15,8876]

def lagger_number(list: list[int]) -> int:
    biggerNumber = list[0]

    for b in list:
        if biggerNumber < b:
            biggerNumber = b

    return biggerNumber

print(lagger_number(numbers))


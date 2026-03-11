numbers = [1,2,3,4,5]

def find_larggerNumber(list: list[int]) -> int:
    laggerNumber = list[0]

    for b in list:
        if laggerNumber < b:
            laggerNumber = b

    return laggerNumber

print(find_larggerNumber(numbers))
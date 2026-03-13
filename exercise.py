numbers = [5,2,8,1,9]

def find_small(numbers: list[int]) -> int:
    smallNumber = numbers[0]

    for s in numbers:
        if smallNumber > s:
            smallNumber = s
    return smallNumber

print(find_small(numbers))
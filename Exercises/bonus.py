numbers = [10,50,7656,1293,1259,122]

def find_number(numbers: list[int]) -> int:
    first = numbers[0]
    second = numbers[0]
    

    for n in numbers:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n

    return second, first
    

print(find_number(numbers))
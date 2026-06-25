numbers = [1,2,3,4,5]

def sum_numbers(list: list[int]) -> int:
    sum = 0

    for s in list:
        sum += s

    return sum

print(sum_numbers(numbers))
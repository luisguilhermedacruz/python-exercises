def find_small(numbers: list[int]) -> int:
    smallNumber = numbers[0]

    for s in numbers:
        if smallNumber > s:
            smallNumber = s
    return smallNumber


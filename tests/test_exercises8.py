from exercise8 import find_small

def test_findsmall():
    numbers = [1,2,3,4,5]
    numbers2 = [10,20,30,40,50]
    assert find_small(numbers) == 1
    assert find_small(numbers2) == 10

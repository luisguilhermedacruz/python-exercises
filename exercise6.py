word = input("")

def count_vowels(word: str) -> int:
    vowels = "aeiou"
    count = 0
    wordLower = word.lower()

    for letter in wordLower:
        if letter in vowels:
            count += 1

    return count

print(count_vowels(word))

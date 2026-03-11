wordSent = input("")

def reverse_string(wordSent):
    reversedWord = ""

    for letter in wordSent:
        reversedWord = letter + reversedWord
    
    return reversedWord

print(reverse_string(wordSent))


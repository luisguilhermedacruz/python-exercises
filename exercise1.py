wordSent = input("")

def character_count(wordSent: str) -> int:
    count = 0
    
    for c in wordSent:
        count += 1
    
    return count

print(character_count(wordSent))


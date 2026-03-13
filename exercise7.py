def reversed_word(word: str) -> str:
    new_word = ""

    for n in word:
        new_word = n + new_word

    return new_word


def unrepeated(string: str) -> str:
    new_word = []

    for char in string:
        if char not in new_word:
            new_word.append(char)

    return "".join(new_word)

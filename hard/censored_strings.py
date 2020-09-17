def uncensor(string: str, letters: str) -> str:
    char_to_replace = "*"
    c_positions = [pos for pos, char in enumerate(string) if char == char_to_replace]

    for index, value in list(zip(c_positions, [vowel for vowel in letters])):
        string = string[:index] + value + string[index + 1:]
    return string

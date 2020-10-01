from typing import List


def split_code(string: str) -> List[str]:
    letter_str = []
    num_str = []

    for char in string:
        if char.isnumeric():
            num_str.append(char)
        else:
            letter_str.append(char)
    return ["".join(letter_str), "".join(num_str)]

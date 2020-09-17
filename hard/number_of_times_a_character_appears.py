from typing import List


def char_appears(string: str, char: str) -> List[int]:
    return [word.lower().count(char) for word in string.split()]

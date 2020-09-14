def sum_of_vowels(string: str) -> int:
    vow_dict = {"a": 4, "e": 3, "i": 1, "o": 0, "u": 0}
    total = 0

    for vow, val in vow_dict.items():
        for letter in string:
            if vow == letter:
                total += vow_dict[val]
    return total

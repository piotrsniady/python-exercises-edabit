def max_separator(string: str) -> list:
    letters = set([char for char in string if string.count(char) > 1])
    letter_dict = {}

    for index, letter in enumerate(string):
        for char in letters:
            if char == letter:
                letter_dict.setdefault(letter, []).append(index)

    longest_letter = []

    for key, value in letter_dict.items():
        substring_len = len(string[value[0]: value[1] + 1])
        max_sub_len = substring_len

        if substring_len >= max_sub_len:
            longest_letter.append(key)
    return longest_letter

def first_before_second(string: str, c1: str, c2: str) -> bool:
    first_char_list_index = []
    second_char_list_index = []

    for index, letter in enumerate(string.lower()):
        if letter == c1:
            first_char_list_index.append(index)
        if letter == c2:
            second_char_list_index.append(index)

    if all(first_char_list_index) > all(second_char_list_index):
        return True
    else:
        return False

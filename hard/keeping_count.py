def keeping_count(string: str) -> str:
    count_dict = dict()

    for letter in string:
        if letter in count_dict.items():
            count_dict[letter] = 1
        else:
            count_dict[letter] += 1

    new_str_list = []

    for i in string:
        for key, value in count_dict.items():
            if i == key:
                new_str_list.append(str(value))
    return "".join(new_str_list)

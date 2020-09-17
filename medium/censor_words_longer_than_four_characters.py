def censor(string: str) -> str:
    string_list = string.split()

    for str_elem in string_list:
        if len(str_elem) > 4:
            string = string.replace(str_elem, "*" * len(str_elem))
    return string

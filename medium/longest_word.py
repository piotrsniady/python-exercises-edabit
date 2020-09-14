def longest_word(string: str) -> str:
    string_list = string.split()
    _longest_word = string_list[0]

    for word in string_list:
        if len(word) > len(_longest_word):
            _longest_word = word
    return _longest_word

def count_uppercase(word_list: list) -> int:
    upper_count = 0

    for word in word_list:
        for letter in word:
            if letter.isupper():
                upper_count += 1

    return upper_count

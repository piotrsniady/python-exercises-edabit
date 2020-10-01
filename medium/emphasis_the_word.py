def emphasis(string: str) -> str:
    for word in string.split():
        if not word.isnumeric():
            upper_word = "".join([word[0].upper() + word[1:] for word in word.split()])
            string = string.replace(word, upper_word)
    return string


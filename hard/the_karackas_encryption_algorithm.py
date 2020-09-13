def karackas_encryption(word: str) -> str:
    dictionary = {
        "a": "0",
        "e": "1",
        "i": "2",
        "o": "3",
        "u": "3"
    }
    word = word[::-1]
    for letter in word:
        if letter in dictionary.keys():
            word = word.replace(letter, dictionary[letter])
    return word


res = karackas_encryption(word="apple")
print(res)

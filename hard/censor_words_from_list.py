def censor_string(txt_str, word_list, char):
    for word in txt_str.split():
        if word in word_list:
            txt_str = txt_str.replace(word, char * len(word))
    return txt_str


res = censor_string(txt_str="Today is a Wednesday!", word_list=["Today", "a"], char="*")
print(res)

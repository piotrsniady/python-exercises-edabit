def add_str_nums(s1: str, s2: str) -> str:
    if s1.isalpha() or s2.isalpha():
        return "-1"
    else:
        if len(s1) == 0:
            s1 = 0
        if len(s2) == 0:
            s2 = 0
        return str(int(s1) + int(s2))

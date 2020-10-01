def match_last_item(lst: list) -> bool:
    joined = "".join(str(i) for i in lst[:-1])

    if joined == lst[-1]:
        return True
    else:
        return False

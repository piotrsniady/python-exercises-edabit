def dominant(lst: list) -> bool:
    pos_set = set()
    neg_set = set()

    for num in lst:
        if num > 0:
            pos_set.add(num)
        else:
            neg_set.add(num)

    if len(pos_set) > len(neg_set):
        return True
    else:
        return False

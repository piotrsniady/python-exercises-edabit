def peel_layer_off(lst: list) -> list:
    lst.pop(0)
    lst.pop(-1)

    for sublist in lst:
        sublist.pop(0)
        sublist.pop(-1)

    return lst

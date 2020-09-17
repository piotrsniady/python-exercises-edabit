def consecutive_combo(l1: list, l2: list) -> bool:
    concat_list = l1 + l2
    concat_list.sort()
    diff_list = [abs(x - y) for x, y in zip(concat_list, concat_list[1:])]

    if len(diff_list) == sum(diff_list):
        return True
    else:
        return False

def median(num_list: list) -> int:
    n = len(num_list)
    num_list.sort()

    if n % 2 == 0:
        med = (num_list[n // 2] + num_list[n // 2 - 1]) / 2
    else:
        med = num_list[n // 2]
    return med

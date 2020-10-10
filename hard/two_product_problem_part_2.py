def two_product(lst: list, n: int) -> list:
    lst_len = len(lst)
    for i in range(0, lst_len - 1):
        for j in range(i + 1, lst_len):
            if lst[i] * lst[j] == n:
                return [lst[i], lst[j]]

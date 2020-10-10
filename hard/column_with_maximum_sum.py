def col_with_max_sum(lst: list, n: int) -> int:
    sub_lists = [lst[i:i + n] for i in range(0, len(lst), n) if len(lst[i:i + n]) == n]
    sum_by_index = [sum(ind_pos) for ind_pos in zip(*sub_lists)]
    min_index = sum_by_index.index(min(sum_by_index))
    print(sum_by_index)
    return min_index + 1

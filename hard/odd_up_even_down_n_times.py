def even_odd_transform(num_list: list, n: int):
    return [x - n * 2 if x % 2 == 0 else x + n * 2 for x in num_list]

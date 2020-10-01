from typing import List


def min_miss_point(lst: list) -> List[int]:
    missing_val = []

    lst.sort()
    pos_val = list(set([val for val in lst if val > 0]))
    gen_num_seq = [i for i in range(min(pos_val), max(pos_val) + 1)]

    for j in gen_num_seq:
        if j not in pos_val:
            missing_val.append(j)

    return missing_val

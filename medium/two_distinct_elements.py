from typing import List


def return_unique(lst: list) -> List[int]:
    num_dict = dict()

    for num in lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    return [key for key, value in num_dict.items() if value == 1]

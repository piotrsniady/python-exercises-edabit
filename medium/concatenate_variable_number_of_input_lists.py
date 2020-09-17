from typing import List


def concat_list(*args: List[int]) -> list:
    flatten_list = []

    for sub_list in args:
        for num in sub_list:
            flatten_list.append(num)

    return flatten_list

from collections import Counter
from typing import Any


def majority_vote(lst: list) -> Any:
    len_of_list = len(lst)
    dict_of_counts = Counter(lst)
    margin = len_of_list / 2

    if len(lst) == 0:
        return None
    else:
        for key, value in dict_of_counts.items():
            if value > margin:
                return key
            else:
                return None


l1 = ["A", "A", "A", "B", "C", "A"]
l2 = ["A", "B", "B", "A", "C", "C"]

res = majority_vote(lst=l1)
print(res)
res = majority_vote(lst=l2)
print(res)

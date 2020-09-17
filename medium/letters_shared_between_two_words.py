def shared_letters(s1: str, s2: str) -> int:
    s1_set = set(s1)
    s2_set = set(s2)
    intersection = len(s1_set.intersection(s2_set))
    return intersection

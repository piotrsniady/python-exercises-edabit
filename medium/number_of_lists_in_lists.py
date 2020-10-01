def num_of_sublists(lst: list) -> int:
    sublist_counter = 0
    for sublist in lst:
        if isinstance(sublist, list):
            sublist_counter += 1
    return sublist_counter

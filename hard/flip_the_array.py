def flip_list(lst: list) -> list:
    if all(isinstance(x, int) for x in lst):
        return [[x] for x in lst]
    else:
        return [item for sublist in lst for item in sublist]

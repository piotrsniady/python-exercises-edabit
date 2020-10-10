def resistance_calculator(lst: list) -> list:
    return [1 / sum([1 / _ for _ in lst]), sum(lst)]

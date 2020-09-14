def is_sastry(num: int) -> bool:
    successor = num + 1
    concat_nums = int(str(num) + str(successor))
    x = concat_nums // 2
    seen = set()

    while x * x != concat_nums:
        x = (x + (concat_nums // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True

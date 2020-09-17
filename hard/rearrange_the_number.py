def rearranged_difference(n: int):
    num_list = [int(x) for x in str(n)]
    num_list.sort()
    desc = num_list[::-1]
    num_list = int("".join([str(x) for x in num_list]))
    desc = int("".join([str(x) for x in desc]))
    return desc - num_list

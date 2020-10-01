def count_missing_nums(lst: list) -> int:
    counter = 0
    nums = []

    for num in lst:
        if num.isnumeric():
            nums.append(int(num))

    gen_list = [j for j in range(min(nums), max(nums) + 1)]

    for gen_num in gen_list:
        if gen_num not in nums:
            counter += 1

    return counter

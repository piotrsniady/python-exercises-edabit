def largest_even(num_list: list) -> int:
    max_val = num_list[0]

    for num in num_list:
        if num % 2 == 0 and num > max_val:
            max_val = num

    return max_val

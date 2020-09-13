def is_equal(num_list: list) -> bool:
    if len(num_list) < 2 or len(num_list) > 2:
        print("The list contains invalid number of elements. Expected 2.")
        quit()
    # elif all([s for s in num_list if s.isdigit()]):
    #     print("Not all elements are numerical.")
    #     quit()
    else:
        summed_list = []
        for num in num_list:
            sum_of_digits = sum(int(digit) for digit in str(num) if digit.isdigit())
            summed_list.append(sum_of_digits)
        if summed_list[1:] == summed_list[:-1]:
            return True
        else:
            return False


res = is_equal([30, 12])
print(res)

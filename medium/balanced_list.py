def balanced(lst: list) -> list:
    if len(lst) % 2 == 0:
        left = lst[0:len(lst) // 2]
        right = lst[len(lst) // 2:]
        sum_left = sum(left)
        sum_right = sum(right)

        if sum_left > sum_right:
            return left + left
        elif sum_left < sum_right:
            return right + right
        else:
            return lst
    else:
        print("Warning. Not even list.")
        quit()

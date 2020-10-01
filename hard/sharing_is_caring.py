def show_the_love(lst: list) -> list:
    quarters = 0

    if lst.count(min(lst)) > 1:
        quit()
    else:
        for index, num in enumerate(lst):
            if num == max(lst):
                lst[index] = num - (num / 4)
                quarters += num / 4

        for ind, n in enumerate(lst):
            if n == min(lst):
                lst[ind] = n + quarters
        return lst

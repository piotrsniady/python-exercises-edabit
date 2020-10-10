def make_box(n: int) -> list:
    mark = "#"
    tmp_index = [_ for _ in range(n)]
    tmp_list = [str(_) for _ in range(n)]
    end_and_beginnng = mark * n

    tmp_list[0] = end_and_beginnng
    tmp_list[-1] = end_and_beginnng

    middle_pattern = "".join((mark + (n - 2) * " " + mark))

    for i in tmp_index[1: -1]:
        tmp_list[i] = middle_pattern

    return tmp_list

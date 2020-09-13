def char_at_pos(num_list, opt):
    positions = []
    for index, value in enumerate(num_list):
        if opt == "even":
            if (index + 1) % 2 == 0:
                positions.append(value)
        elif opt == "odd":
            if (index + 1) % 2 != 0:
                positions.append(value)
    return positions


res = char_at_pos(num_list=[2, 4, 6, 8, 10], opt="odd")
print(res)

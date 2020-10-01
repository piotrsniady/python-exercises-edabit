from re import findall


def get_prices(lst: list):
    flatten_list = []

    prices = [findall(pattern=r'\d+.\d+', string=i) for i in lst]

    for sublist in prices:
        for sub_value in sublist:
            flatten_list.append(float(sub_value))
    return flatten_list

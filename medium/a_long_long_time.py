from operator import itemgetter


def longest_time(h: int, m: int, s: int) -> int:
    h_to_s = h * 60 * 60
    m_to_s = m * 60

    index, value = max(enumerate([h_to_s, m_to_s, s]), key=itemgetter(1))

    if index == 0:
        return h
    elif index == 1:
        return m
    else:
        return s

def solve():
    """Index: 224.
    Returns: the age of the fifth scroll.
    """
    # L1
    first_scroll_age = 4080 # The first scroll is 4080 years old
    half_divisor = 2 # half as many years
    second_scroll_age = first_scroll_age + first_scroll_age / half_divisor

    # L2
    third_scroll_age = second_scroll_age + second_scroll_age / half_divisor

    # L3
    fourth_scroll_age = third_scroll_age + third_scroll_age / half_divisor

    # L4
    fifth_scroll_age = fourth_scroll_age + fourth_scroll_age / half_divisor

    # FA
    answer = fifth_scroll_age
    return answer
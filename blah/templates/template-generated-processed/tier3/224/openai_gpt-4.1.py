def solve():
    """Index: 224.
    Returns: the age of the fifth scroll in years.
    """
    # L1
    first_scroll_age = 4080 # The first scroll is 4080 years old
    second_scroll_age = first_scroll_age + first_scroll_age / 2

    # L2
    third_scroll_age = second_scroll_age + second_scroll_age / 2

    # L3
    fourth_scroll_age = third_scroll_age + third_scroll_age / 2

    # L4
    fifth_scroll_age = fourth_scroll_age + fourth_scroll_age / 2

    # FA
    answer = fifth_scroll_age
    return answer
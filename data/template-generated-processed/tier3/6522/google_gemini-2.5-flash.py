def solve():
    """Index: 6522.
    Returns: the total number of skips made across all throws.
    """
    # L1
    fifth_throw_skips = 8 # If his fifth throw skipped 8 times
    one_more_than_fourth = 1 # one more time than the fourth throw
    fourth_throw_skips = fifth_throw_skips - one_more_than_fourth

    # L2
    three_fewer_than_third = 3 # 3 fewer times than his third throw
    third_throw_skips = fourth_throw_skips + three_fewer_than_third

    # L3
    twice_as_many = 2 # skips twice as many times as his second
    second_throw_skips = third_throw_skips / twice_as_many

    # L4
    two_more_than_first = 2 # skips two more times across the water than his first
    first_throw_skips = second_throw_skips - two_more_than_first

    # L5
    total_skips = fifth_throw_skips + fourth_throw_skips + third_throw_skips + second_throw_skips + first_throw_skips

    # FA
    answer = total_skips
    return answer
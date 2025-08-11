def solve():
    """Index: 4130.
    Returns: the total pounds Kyle can lift in all.
    """
    # L1
    more_pounds_this_year = 60 # 60 more pounds this year
    times_as_much = 3 # 3 times as much as he could lift last year
    pounds_last_year = more_pounds_this_year / times_as_much

    # L2
    total_pounds_now = more_pounds_this_year + pounds_last_year

    # FA
    answer = total_pounds_now
    return answer
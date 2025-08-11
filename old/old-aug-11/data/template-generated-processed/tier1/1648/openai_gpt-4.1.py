def solve():
    """Index: 1648.
    Returns: the number of jumping jacks Kenny must do on Saturday to beat last week's total.
    """
    # L1
    sunday = 34 # on Sunday he did 34
    monday = 20 # on Monday he did 20
    wednesday = 123 # on Wednesday he did 123
    thursday = 64 # on Thursday he did 64
    friday = 23 # on Friday he did 23
    total_so_far = sunday + monday + wednesday + thursday + friday

    # L2
    last_week_total = 324 # last week he did 324 total jumping jacks
    to_tie = last_week_total - total_so_far

    # L3
    one_more = 1 # WK
    to_beat = to_tie + one_more

    # FA
    answer = to_beat
    return answer
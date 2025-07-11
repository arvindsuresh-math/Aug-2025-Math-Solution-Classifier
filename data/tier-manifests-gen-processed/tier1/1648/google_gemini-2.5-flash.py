def solve():
    """Index: 1648.
    Returns: the number of jumping jacks Kenny has to do on Saturday to beat last week's number.
    """
    # L1
    sunday_jacks = 34 # on Sunday he did 34
    monday_jacks = 20 # On Monday he did 20
    wednesday_jacks = 123 # On Wednesday he did 123
    thursday_jacks = 64 # On Thursday he did 64
    friday_jacks = 23 # On Friday he did 23
    jacks_done_this_week = sunday_jacks + monday_jacks + wednesday_jacks + thursday_jacks + friday_jacks

    # L2
    last_week_total_jacks = 324 # last week he did 324 total jumping jacks
    jacks_to_match_last_week = last_week_total_jacks - jacks_done_this_week

    # L3
    one_more_jack = 1 # to make sure he beats last week's number
    jacks_needed_saturday = jacks_to_match_last_week + one_more_jack

    # FA
    answer = jacks_needed_saturday
    return answer
def solve():
    """Index: 727.
    Returns: the total number of shells Shara has now.
    """
    # L1
    shells_per_day = 5 # found 5 shells per day
    num_days = 3 # for 3 days
    shells_first_three_days = shells_per_day * num_days

    # L2
    shells_fourth_day = 6 # found 6 shells on the fourth day
    shells_vacation = shells_first_three_days + shells_fourth_day

    # L3
    initial_shells = 20 # had 20 shells before she went on vacation
    total_shells = initial_shells + shells_vacation

    # FA
    answer = total_shells
    return answer
def solve():
    """Index: 3580.
    Returns: the number of seedlings Remi's father planted.
    """
    # L1
    multiplier_second_day = 2 # twice the number of seedlings
    seedlings_first_day = 200 # planted 200 seedlings on the farm
    seedlings_second_day = multiplier_second_day * seedlings_first_day

    # L2
    remi_total_two_days = seedlings_second_day + seedlings_first_day

    # L3
    total_transferred = 1200 # total number of seedlings transferred to the farm on these two days was 1200
    father_planted = total_transferred - remi_total_two_days

    # FA
    answer = father_planted
    return answer
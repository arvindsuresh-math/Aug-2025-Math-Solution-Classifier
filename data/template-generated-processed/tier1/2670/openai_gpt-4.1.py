def solve():
    """Index: 2670.
    Returns: the total number of people counted on the two days.
    """
    # L1
    multiplier_first_day = 2 # number of people counted on the first day was twice the total number counted on the second day
    second_day_count = 500 # 500 people were counted on the second day
    first_day_count = multiplier_first_day * second_day_count

    # L2
    total_count = first_day_count + second_day_count

    # FA
    answer = total_count
    return answer
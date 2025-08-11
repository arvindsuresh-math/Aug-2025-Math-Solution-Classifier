def solve():
    """Index: 3001.
    Returns: the total number of miles the ladies walk.
    """
    # L1
    num_other_ladies = 4 # with 4 other ladies
    num_ladies_in_group = num_other_ladies + 1
    group_daily_miles = 3 # all walk 3 miles together
    num_days_walked = 6 # for 6 days
    group_total_miles = group_daily_miles * num_days_walked

    # L2
    jamie_additional_daily_miles = 2 # Jamie walks an additional 2 miles per day
    jamie_additional_total_miles = jamie_additional_daily_miles * num_days_walked

    # L3
    sue_half_divisor = 2 # walks half that amount
    sue_total_miles = jamie_additional_total_miles / sue_half_divisor

    # L4
    total_miles_walked = group_total_miles + jamie_additional_total_miles + sue_total_miles

    # FA
    answer = total_miles_walked
    return answer
def solve():
    """Index: 1551.
    Returns: the total time students spend in time-out.
    """
    # L1
    running_time_outs = 5 # 5 time-outs for running
    multiplier_for_throwing = 5 # five times that number
    base_for_throwing = running_time_outs * multiplier_for_throwing

    # L2
    subtraction_for_throwing = 1 # 1 less than five times that number
    throwing_food_time_outs = base_for_throwing - subtraction_for_throwing

    # L3
    divisor_for_swearing = 3 # 1/3 the number of food-throwing time-outs
    swearing_time_outs = throwing_food_time_outs / divisor_for_swearing

    # L4
    total_time_outs_count = swearing_time_outs + throwing_food_time_outs + running_time_outs

    # L5
    minutes_per_time_out = 5 # each time-out is 5 minutes
    total_time_in_minutes = total_time_outs_count * minutes_per_time_out

    # FA
    answer = total_time_in_minutes
    return answer
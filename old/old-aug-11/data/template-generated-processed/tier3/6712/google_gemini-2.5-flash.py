def solve():
    """Index: 6712.
    Returns: the average speed Candace can go in the new shoes.
    """
    # L1
    old_shoes_speed = 6 # 6 miles per hour in the old shoes
    speed_multiplier = 2 # walk twice as fast
    initial_new_shoes_speed = old_shoes_speed * speed_multiplier

    # L2
    speed_reduction_per_blister = 2 # Each blister slows Candance down by 2 miles per hour
    speed_after_first_blister = initial_new_shoes_speed - speed_reduction_per_blister

    # L4
    number_of_speeds_to_average = 2 # average the two speeds
    overall_average_speed = (initial_new_shoes_speed + speed_after_first_blister) / number_of_speeds_to_average

    # FA
    answer = overall_average_speed
    return answer
def solve():
    """Index: 6773.
    Returns: the amount Jerry needs to earn tonight to meet his average tip goal.
    """
    # L1
    num_days_work = 5 # five days a week
    desired_average_per_night = 50 # average of $50 in tips per night
    total_needed_for_average = num_days_work * desired_average_per_night

    # L2
    tip1 = 20 # earned $20
    tip2 = 60 # earned $60
    tip3 = 15 # earned $15
    tip4 = 40 # earned $40
    total_earned_past_four_nights = tip1 + tip2 + tip3 + tip4

    # L3
    needed_tonight = total_needed_for_average - total_earned_past_four_nights

    # FA
    answer = needed_tonight
    return answer
def solve():
    """Index: 5811.
    Returns: the total money earned in September and October.
    """
    # L1
    mowing_hours_september = 25 # mowed lawns for 25 hours
    mowing_rate = 4 # charges $4 an hour for mowing lawns
    earned_mowing_september = mowing_hours_september * mowing_rate

    # L2
    weeding_hours_september = 3 # pulled weeds for 3 hours
    weeding_rate = 8 # $8 for pulling weeds
    earned_weeding_september = weeding_hours_september * weeding_rate

    # L3
    total_earned_september = earned_mowing_september + earned_weeding_september

    # L4
    num_months = 2 # If she worked the same number of hours in October
    total_earned_two_months = total_earned_september * num_months

    # FA
    answer = total_earned_two_months
    return answer
def solve():
    """Index: 990.
    Returns: the total money Grace earned in September.
    """
    # L1
    hours_mowing = 63 # mowed lawns for 63 hours
    charge_mowing = 6 # charges $6 an hour for mowing lawns
    earned_mowing = hours_mowing * charge_mowing

    # L2
    hours_weeding = 9 # pulled weeds for 9 hours
    charge_weeding = 11 # $11 for pulling weeds
    earned_weeding = hours_weeding * charge_weeding

    # L3
    hours_mulching = 10 # put down mulch for 10 hours
    charge_mulching = 9 # $9 for putting down mulch
    earned_mulching = hours_mulching * charge_mulching

    # L4
    total_earned = earned_mowing + earned_weeding + earned_mulching

    # FA
    answer = total_earned
    return answer
def solve():
    """Index: 1853.
    Returns: the total number of shirts Shenny should pack for her vacation.
    """
    # L1
    total_days_vacation = 7 # WK
    days_same_shirt = 2 # departing on Monday and returning on Sunday
    days_needing_different_shirts = total_days_vacation - days_same_shirt

    # L2
    shirts_per_other_day = 2 # two different shirts each other day
    shirts_for_other_days = shirts_per_other_day * days_needing_different_shirts

    # L3
    shirt_for_mon_sun = 1 # use the same shirt when departing on Monday and returning on Sunday
    total_shirts_needed = shirts_for_other_days + shirt_for_mon_sun

    # FA
    answer = total_shirts_needed
    return answer
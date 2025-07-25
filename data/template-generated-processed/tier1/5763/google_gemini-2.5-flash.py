def solve():
    """Index: 5763.
    Returns: the total earnings in three days.
    """
    # L1
    friday_earnings = 147 # raised $147 on Friday
    multiplier_for_twice = 2 # twice their Friday earnings
    twice_friday_earnings = friday_earnings * multiplier_for_twice

    # L2
    saturday_more_than_twice = 7 # $7 more than twice their Friday earnings
    saturday_earnings = twice_friday_earnings + saturday_more_than_twice

    # L3
    sunday_more_than_friday = 78 # $78 more than their earnings on Friday
    sunday_earnings = friday_earnings + sunday_more_than_friday

    # L4
    total_earnings = friday_earnings + saturday_earnings + sunday_earnings

    # FA
    answer = total_earnings
    return answer
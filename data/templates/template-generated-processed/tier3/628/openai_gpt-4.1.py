def solve():
    """Index: 628.
    Returns: the number of hours Alani needs to baby-sit to earn $75 at the same rate.
    """
    # L1
    earned = 45 # Alani earned $45
    hours = 3 # for 3 hours of baby-sitting
    rate = earned / hours

    # L2
    target_earnings = 75 # to earn $75
    required_hours = target_earnings / rate

    # FA
    answer = required_hours
    return answer
def solve():
    """Index: 1573.
    Returns: the total number of hours Oliver worked out during the four days.
    """
    # L1
    monday_hours = 4 # worked out for 4 hours on Monday
    tuesday_less = 2 # next day for 2 hours less
    tuesday_hours = monday_hours - tuesday_less

    # L2
    wednesday_multiplier = 2 # twice as much as on Monday
    wednesday_hours = wednesday_multiplier * monday_hours

    # L3
    thursday_multiplier = 2 # twice as much time as on Tuesday
    thursday_hours = thursday_multiplier * tuesday_hours

    # L4
    total_hours = monday_hours + tuesday_hours + wednesday_hours + thursday_hours

    # FA
    answer = total_hours
    return answer
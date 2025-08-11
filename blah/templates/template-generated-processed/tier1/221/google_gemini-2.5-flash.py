def solve():
    """Index: 221.
    Returns: the total number of miles Mira can jog for five days.
    """
    # L1
    miles_per_hour = 5 # 5 miles per hour
    hours_per_day = 2 # 2 hours every morning
    miles_per_day = miles_per_hour * hours_per_day

    # L2
    num_days = 5 # for five days
    total_miles = miles_per_day * num_days

    # FA
    answer = total_miles
    return answer
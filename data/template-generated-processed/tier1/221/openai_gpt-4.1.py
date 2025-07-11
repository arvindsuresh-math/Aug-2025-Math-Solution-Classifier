def solve():
    """Index: 221.
    Returns: the total number of miles Mira can jog in five days.
    """
    # L1
    miles_per_hour = 5 # jogs 5 miles per hour
    hours_per_day = 2 # jogs for 2 hours every morning
    miles_per_day = miles_per_hour * hours_per_day

    # L2
    num_days = 5 # five days
    total_miles = miles_per_day * num_days

    # FA
    answer = total_miles
    return answer
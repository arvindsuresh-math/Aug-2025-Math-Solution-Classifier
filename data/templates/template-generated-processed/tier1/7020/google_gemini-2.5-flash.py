def solve():
    """Index: 7020.
    Returns: the total number of miles Emberly walked in March.
    """
    # L1
    days_in_march = 31 # WK
    days_not_walked = 4 # didn't walk for 4 days in March
    days_walked = days_in_march - days_not_walked

    # L2
    hours_per_walk = 1 # each walk takes her 1 hour
    total_hours_walked = days_walked * hours_per_walk

    # L3
    miles_per_walk = 4 # covering 4 miles
    total_miles_walked = total_hours_walked * miles_per_walk

    # FA
    answer = total_miles_walked
    return answer
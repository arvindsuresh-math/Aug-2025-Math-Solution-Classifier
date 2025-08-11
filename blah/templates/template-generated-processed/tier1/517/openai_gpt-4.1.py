def solve():
    """Index: 517.
    Returns: the total number of miles Roger rode his bike for in a day.
    """
    # L1
    morning_miles = 2 # 2 miles this morning
    evening_multiplier = 5 # 5 times that amount in the evening
    evening_miles = evening_multiplier * morning_miles

    # L2
    total_miles = morning_miles + evening_miles

    # FA
    answer = total_miles
    return answer
def solve():
    """Index: 517.
    Returns: the total miles Roger rode his bike.
    """
    # L1
    morning_miles = 2 # 2 miles this morning
    multiplier_evening = 5 # 5 times that amount
    evening_miles = multiplier_evening * morning_miles

    # L2
    total_miles = morning_miles + evening_miles

    # FA
    answer = total_miles
    return answer
def solve():
    """Index: 1996.
    Returns: the total number of flowers Ali sells.
    """
    # L1
    flowers_monday = 4 # 4 flowers on Monday
    flowers_tuesday = 8 # 8 flowers on Tuesday
    monday_tuesday_total = flowers_monday + flowers_tuesday

    # L2
    multiplier_double = 2 # double the number of flowers
    flowers_friday = multiplier_double * flowers_monday

    # L3
    total_flowers_sold = monday_tuesday_total + flowers_friday

    # FA
    answer = total_flowers_sold
    return answer
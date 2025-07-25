def solve():
    """Index: 1996.
    Returns: the total number of flowers Ali sold.
    """
    # L1
    monday_flowers = 4 # sold 4 flowers on Monday
    tuesday_flowers = 8 # 8 flowers on Tuesday
    mon_tue_total = monday_flowers + tuesday_flowers

    # L2
    double = 2 # double the number of flowers he sold on Monday
    friday_flowers = double * monday_flowers

    # L3
    total_flowers = mon_tue_total + friday_flowers

    # FA
    answer = total_flowers
    return answer
def solve():
    """Index: 2022.
    Returns: the number of days the 2-liter bottle of soda will last.
    """
    # L1
    bottle_liters = 2 # a 2-liter bottle of soda
    ml_per_liter = 1000 # 1,000 ml in 1 liter
    bottle_ml = bottle_liters * ml_per_liter

    # L2
    daily_consumption_ml = 500 # 500 ml bottle of soda each day
    days_last = bottle_ml / daily_consumption_ml

    # FA
    answer = days_last
    return answer
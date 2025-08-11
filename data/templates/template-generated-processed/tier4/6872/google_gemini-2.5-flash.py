def solve():
    """Index: 6872.
    Returns: the number of glasses of water Mary should drink per day.
    """
    # L1
    daily_water_liters = 1.5 # 1.5 liters of water a day
    ml_per_liter = 1000 # WK
    daily_water_ml = daily_water_liters * ml_per_liter

    # L2
    glass_capacity_ml = 250 # glasses hold 250 mL of water
    num_glasses = daily_water_ml / glass_capacity_ml

    # FA
    answer = num_glasses
    return answer
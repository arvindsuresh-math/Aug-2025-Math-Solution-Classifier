def solve():
    """Index: 3557.
    Returns: the number of times people can jump in the pool before Jim has to clean it.
    """
    # L1
    pool_capacity_L = 2000 # the pool holds 2000 L of water
    full_percentage_decimal = 0.8 # 80% full
    water_at_80_percent_L = pool_capacity_L * full_percentage_decimal

    # L2
    splash_out_capacity_L = pool_capacity_L - water_at_80_percent_L

    # L3
    ml_per_L = 1000 # WK
    splash_out_capacity_ml = splash_out_capacity_L * ml_per_L

    # L4
    water_splash_per_jump_ml = 400 # 400 ml of water to splash out
    num_jumps_before_cleaning = splash_out_capacity_ml / water_splash_per_jump_ml

    # FA
    answer = num_jumps_before_cleaning
    return answer
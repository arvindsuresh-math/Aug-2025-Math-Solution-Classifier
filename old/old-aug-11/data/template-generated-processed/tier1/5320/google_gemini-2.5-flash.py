def solve():
    """Index: 5320.
    Returns: the amount of water left in the bathtub in milliliters.
    """
    # L1
    faucet_rate_ml_per_minute = 40 # 40 ml/minute
    minutes_per_hour = 60 # WK
    fill_rate_ml_per_hour = faucet_rate_ml_per_minute * minutes_per_hour

    # L2
    evaporation_rate_ml_per_hour = 200 # 200 ml/hour
    net_add_rate_ml_per_hour = fill_rate_ml_per_hour - evaporation_rate_ml_per_hour

    # L3
    running_hours = 9 # 9 hours
    total_water_added_ml = net_add_rate_ml_per_hour * running_hours

    # L4
    liters_dumped = 12 # 12 liters
    ml_per_liter = 1000 # WK
    dumped_ml = liters_dumped * ml_per_liter

    # L5
    remaining_water_ml = total_water_added_ml - dumped_ml

    # FA
    answer = remaining_water_ml
    return answer
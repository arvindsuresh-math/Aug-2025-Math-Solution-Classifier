def solve():
    """Index: 26.
    Returns: the number of ml of salt Jack will get.
    """
    # L1
    seawater_volume_liters = 2 # 2 liters of seawater
    salt_percentage_num = 20 # 20% salt
    percent_to_decimal_factor = 0.01 # WK
    salt_volume_liters = seawater_volume_liters * salt_percentage_num * percent_to_decimal_factor

    # L2
    ml_per_liter = 1000 # WK
    salt_volume_ml = salt_volume_liters * ml_per_liter

    # FA
    answer = salt_volume_ml
    return answer
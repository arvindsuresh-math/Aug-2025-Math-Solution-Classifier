def solve():
    """Index: 26.
    Returns: the number of ml of salt Jack will get when all the water evaporates.
    """
    # L1
    seawater_liters = 2 # collects 2 liters of seawater
    salt_percent = 20 # water is 20% salt
    percent_factor = 0.01 # WK
    salt_liters = seawater_liters * salt_percent * percent_factor

    # L2
    ml_per_liter = 1000 # WK
    salt_ml = salt_liters * ml_per_liter

    # FA
    answer = salt_ml
    return answer
def solve():
    """Index: 5863.
    Returns: the total volume of the quiche.
    """
    # L1
    raw_spinach_volume = 40 # 40 ounces of raw spinach
    volume_reduction_percent = 20 # 20% of its initial volume
    percent_factor = 0.01 # WK
    cooked_spinach_volume = raw_spinach_volume * volume_reduction_percent * percent_factor

    # L2
    cream_cheese_volume = 6 # 6 ounces of cream cheese
    eggs_volume = 4 # 4 ounces of eggs
    total_volume = cooked_spinach_volume + cream_cheese_volume + eggs_volume

    # FA
    answer = total_volume
    return answer
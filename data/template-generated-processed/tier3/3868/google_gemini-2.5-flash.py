def solve():
    """Index: 3868.
    Returns: the number of liters left in the barrel.
    """
    # L1
    initial_volume = 220 # A 220-liter barrel
    percentage_lost = 10 # lost 10% of its contents
    divisor_for_percentage = 100 # WK
    liters_lost = initial_volume * percentage_lost / divisor_for_percentage

    # L2
    liters_left = initial_volume - liters_lost

    # FA
    answer = liters_left
    return answer
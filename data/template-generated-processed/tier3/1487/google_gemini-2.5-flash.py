def solve():
    """Index: 1487.
    Returns: the total number of eggs all hens will lay in 15 days.
    """
    # L1
    initial_hens = 10 # 10 hens
    initial_eggs = 80 # 80 eggs
    days_L1 = 10 # in 10 days
    eggs_per_hen_10_days = initial_eggs / initial_hens

    # L2
    divisor_L2 = 2 # WK
    target_days_L2 = 5 # in 5 days
    eggs_per_hen_5_days = eggs_per_hen_10_days / divisor_L2

    # L3
    target_days_L3 = 15 # in 15 days
    multiplier_L3 = 3 # WK
    eggs_per_hen_15_days = eggs_per_hen_5_days * multiplier_L3

    # L4
    new_hens = 15 # 15 more hens
    total_hens = initial_hens + new_hens
    total_eggs_15_days = total_hens * eggs_per_hen_15_days

    # FA
    answer = total_eggs_15_days
    return answer
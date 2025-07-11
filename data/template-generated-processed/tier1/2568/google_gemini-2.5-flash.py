def solve():
    """Index: 2568.
    Returns: the total number of yolks in the carton.
    """
    # L1
    total_eggs_in_carton = 12 # One carton of 12 eggs
    eggs_with_double_yolks = 5 # five eggs with double yolks
    eggs_with_single_yolk = total_eggs_in_carton - eggs_with_double_yolks

    # L2
    yolks_per_double_yolk_egg = 2 # double yolks
    yolks_from_double_yolk_eggs = eggs_with_double_yolks * yolks_per_double_yolk_egg

    # L3
    total_yolks = eggs_with_single_yolk + yolks_from_double_yolk_eggs

    # FA
    answer = total_yolks
    return answer
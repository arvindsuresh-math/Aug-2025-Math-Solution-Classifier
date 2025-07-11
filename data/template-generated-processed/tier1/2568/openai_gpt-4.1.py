def solve():
    """Index: 2568.
    Returns: the total number of yolks in the whole carton.
    """
    # L1
    total_eggs = 12 # One carton of 12 eggs
    double_yolk_eggs = 5 # five eggs with double yolks
    single_yolk_eggs = total_eggs - double_yolk_eggs

    # L2
    yolks_per_double_egg = 2 # WK
    yolks_from_double = double_yolk_eggs * yolks_per_double_egg

    # L3
    total_yolks = single_yolk_eggs + yolks_from_double

    # FA
    answer = total_yolks
    return answer
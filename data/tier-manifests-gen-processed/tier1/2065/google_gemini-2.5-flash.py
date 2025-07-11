def solve():
    """Index: 2065.
    Returns: the number of eggs Myrtle has after dropping some.
    """
    # L1
    num_hens = 3 # 3 hens
    eggs_per_hen_per_day = 3 # lay 3 eggs a day
    eggs_per_day = num_hens * eggs_per_hen_per_day

    # L2
    days_gone = 7 # gone for 7 days
    total_eggs_uncollected = eggs_per_day * days_gone

    # L3
    neighbor_took = 12 # neighbor took 12 eggs
    eggs_after_neighbor = total_eggs_uncollected - neighbor_took

    # L4
    myrtle_dropped = 5 # dropping 5 on the way
    final_eggs = eggs_after_neighbor - myrtle_dropped

    # FA
    answer = final_eggs
    return answer
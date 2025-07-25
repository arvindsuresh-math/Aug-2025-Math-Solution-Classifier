def solve():
    """Index: 2065.
    Returns: the number of eggs Myrtle has after returning home and dropping some eggs.
    """
    # L1
    num_hens = 3 # Myrtle’s 3 hens
    eggs_per_hen_per_day = 3 # lay 3 eggs a day
    eggs_per_day = num_hens * eggs_per_hen_per_day

    # L2
    days_away = 7 # gone for 7 days
    total_eggs = eggs_per_day * days_away

    # L3
    neighbor_took = 12 # neighbor took 12 eggs
    eggs_after_neighbor = total_eggs - neighbor_took

    # L4
    eggs_dropped = 5 # dropping 5 on the way into her house
    eggs_remaining = eggs_after_neighbor - eggs_dropped

    # FA
    answer = eggs_remaining
    return answer
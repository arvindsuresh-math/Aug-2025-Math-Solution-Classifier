def solve():
    """Index: 1621.
    Returns: the total number of bacon strips the cook needs to fry.
    """
    # L1
    eggs_per_plate = 2 # two eggs
    bacon_multiplier = 2 # twice as many bacon strips as eggs
    bacon_strips_per_plate = eggs_per_plate * bacon_multiplier

    # L2
    num_customers = 14 # 14 customers
    total_bacon_strips = num_customers * bacon_strips_per_plate

    # FA
    answer = total_bacon_strips
    return answer
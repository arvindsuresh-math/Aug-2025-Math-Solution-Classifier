def solve():
    """Index: 1621.
    Returns: the total number of bacon strips the cook needs to fry for 14 breakfast plates.
    """
    # L1
    eggs_per_plate = 2 # two eggs
    bacon_per_egg = 2 # twice as many bacon strips as eggs
    bacon_per_plate = eggs_per_plate * bacon_per_egg

    # L2
    num_customers = 14 # 14 customers order breakfast plates
    total_bacon = num_customers * bacon_per_plate

    # FA
    answer = total_bacon
    return answer
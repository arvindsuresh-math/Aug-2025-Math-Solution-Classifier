def solve():
    """Index: 2208.
    Returns: the total number of feet of wood Steve needs to buy.
    """
    # L1
    num_lengths_4ft = 6 # 6 lengths of wood that measure 4 feet
    length_4ft = 4 # 4 feet
    total_4ft = num_lengths_4ft * length_4ft

    # L2
    num_lengths_2ft = 2 # 2 lengths of wood that measure 2 feet
    length_2ft = 2 # 2 feet
    total_2ft = num_lengths_2ft * length_2ft

    # L3
    total_feet = total_4ft + total_2ft

    # FA
    answer = total_feet
    return answer
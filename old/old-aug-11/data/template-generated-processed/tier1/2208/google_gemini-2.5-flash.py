def solve():
    """Index: 2208.
    Returns: the total feet of wood Steve needs to buy.
    """
    # L1
    num_lengths_4ft = 6 # 6 lengths of wood
    length_per_4ft = 4 # 4 feet
    total_4ft_wood = num_lengths_4ft * length_per_4ft

    # L2
    num_lengths_2ft = 2 # 2 lengths of wood
    length_per_2ft = 2 # 2 feet
    total_2ft_wood = num_lengths_2ft * length_per_2ft

    # L3
    total_wood_needed = total_4ft_wood + total_2ft_wood

    # FA
    answer = total_wood_needed
    return answer
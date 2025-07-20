def solve():
    """Index: 4411.
    Returns: the total time it takes for Alexis to sew 6 skirts and 4 coats.
    """
    # L1
    time_per_skirt = 2 # a skirt in 2 hours
    num_skirts = 6 # 6 skirts
    time_for_skirts = time_per_skirt * num_skirts

    # L2
    time_per_coat = 7 # a coat in 7 hours
    num_coats = 4 # 4 coats
    time_for_coats = time_per_coat * num_coats

    # L3
    total_time = time_for_skirts + time_for_coats

    # FA
    answer = total_time
    return answer
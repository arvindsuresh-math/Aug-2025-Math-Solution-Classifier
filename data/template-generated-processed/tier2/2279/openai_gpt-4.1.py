def solve():
    """Index: 2279.
    Returns: the number of shoes Austin still needs to polish.
    """
    # L1
    num_pairs = 10 # 10 pairs of dress shoes
    shoes_per_pair = 2 # each pair is made of 2 individual shoes
    total_shoes = num_pairs * shoes_per_pair

    # L2
    percent_polished_num = 45 # 45% of individual shoes
    percent_polished_decimal = 0.45 # .45*20
    percent_factor = 0.01 # WK
    polished_shoes = percent_polished_num * percent_factor * total_shoes

    # L3
    shoes_left = total_shoes - polished_shoes

    # FA
    answer = shoes_left
    return answer
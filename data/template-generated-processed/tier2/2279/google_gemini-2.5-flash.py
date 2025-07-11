def solve():
    """Index: 2279.
    Returns: the number of additional shoes Austin needs to polish.
    """
    # L1
    num_pairs_shoes = 10 # 10 pairs of dress shoes
    shoes_per_pair = 2 # WK
    total_individual_shoes = num_pairs_shoes * shoes_per_pair

    # L2
    polished_percent_decimal = 0.45 # 45% of individual shoes
    polished_percent_num = 45 # 45%
    percent_factor = 0.01 # WK
    polished_shoes_count = polished_percent_decimal * total_individual_shoes

    # L3
    remaining_shoes_to_polish = total_individual_shoes - polished_shoes_count

    # FA
    answer = remaining_shoes_to_polish
    return answer
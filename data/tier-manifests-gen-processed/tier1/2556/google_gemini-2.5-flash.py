def solve():
    """Index: 2556.
    Returns: the total weight of 7 white rhinos and 8 black rhinos in pounds.
    """
    # L1
    white_rhino_single_weight_lbs = 5100 # One white rhino weighs 5100 pounds
    num_white_rhinos = 7 # 7 white rhinos
    total_weight_white_rhinos_lbs = white_rhino_single_weight_lbs * num_white_rhinos

    # L2
    black_rhino_single_weight_ton = 1 # one black rhino weighs 1 ton
    pounds_per_ton = 2000 # WK
    black_rhino_single_weight_lbs = black_rhino_single_weight_ton * pounds_per_ton

    # L3
    num_black_rhinos = 8 # 8 black rhinos
    total_weight_black_rhinos_lbs = num_black_rhinos * black_rhino_single_weight_lbs

    # L4
    total_combined_weight_lbs = total_weight_white_rhinos_lbs + total_weight_black_rhinos_lbs

    # FA
    answer = total_combined_weight_lbs
    return answer
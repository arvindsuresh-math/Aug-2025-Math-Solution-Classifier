def solve():
    """Index: 2556.
    Returns: the total weight in pounds of 7 white rhinos and 8 black rhinos.
    """
    # L1
    white_rhino_weight = 5100 # One white rhino weighs 5100 pounds
    num_white_rhinos = 7 # 7 white rhinos
    total_white_rhino_weight = white_rhino_weight * num_white_rhinos

    # L2
    ton = 2000 # 1 ton = 2000 pounds # WK
    
    # L3
    num_black_rhinos = 8 # 8 black rhinos
    black_rhino_weight = ton # one black rhino weighs 1 ton
    total_black_rhino_weight = num_black_rhinos * black_rhino_weight

    # L4
    total_weight = total_white_rhino_weight + total_black_rhino_weight

    # FA
    answer = total_weight
    return answer
def solve():
    """Index: 3598.
    Returns: the number of pieces of macarons that were eaten.
    """
    # L1
    num_dozens = 3 # 3 dozens of macarons
    dozen = 12 # WK
    macarons_from_dozens = num_dozens * dozen

    # L2
    initial_pieces = 10 # her 10 pieces of macarons
    total_macarons = macarons_from_dozens + initial_pieces

    # L3
    left_over_macarons = 15 # 15 pieces of macarons are left over
    macarons_eaten = total_macarons - left_over_macarons

    # FA
    answer = macarons_eaten
    return answer
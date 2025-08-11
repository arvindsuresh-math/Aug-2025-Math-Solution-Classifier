def solve():
    """Index: 7437.
    Returns: the number of quadruple pieces sold.
    """
    # L1
    num_sellers = 2 # Michael and Thomas
    earnings_per_person = 5 # earned $5 each
    total_earnings = num_sellers * earnings_per_person

    # L2
    num_single_pieces = 100 # 100 single pieces
    cost_per_circle_decimal = 0.01 # WK
    earnings_single_pieces = num_single_pieces * cost_per_circle_decimal

    # L3
    num_double_pieces = 45 # 45 double pieces
    cost_double_piece_decimal = 0.02 # WK
    earnings_double_pieces = num_double_pieces * cost_double_piece_decimal

    # L4
    num_triple_pieces = 50 # 50 triple pieces
    cost_triple_piece_decimal = 0.03 # WK
    earnings_triple_pieces = num_triple_pieces * cost_triple_piece_decimal

    # L5
    earnings_first_three_types = earnings_single_pieces + earnings_double_pieces + earnings_triple_pieces

    # L6
    earnings_quadruple_pieces = total_earnings - earnings_first_three_types

    # L7
    cost_quadruple_piece_decimal = 0.04 # WK
    num_quadruple_pieces = earnings_quadruple_pieces / cost_quadruple_piece_decimal

    # FA
    answer = num_quadruple_pieces
    return answer
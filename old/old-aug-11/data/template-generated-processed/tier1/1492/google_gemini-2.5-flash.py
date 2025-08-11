def solve():
    """Index: 1492.
    Returns: the total number of pairs of shoes Ellie and Riley have.
    """
    # L1
    ellie_shoes = 8 # Ellie has 8 pairs of shoes
    riley_fewer = 3 # Riley has 3 fewer
    riley_shoes = ellie_shoes - riley_fewer

    # L2
    total_shoes = ellie_shoes + riley_shoes

    # FA
    answer = total_shoes
    return answer
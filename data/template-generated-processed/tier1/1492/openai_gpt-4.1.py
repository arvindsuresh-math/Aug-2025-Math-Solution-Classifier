def solve():
    """Index: 1492.
    Returns: the total number of pairs of shoes Ellie and Riley have together.
    """
    # L1
    ellie_pairs = 8 # Ellie has 8 pairs of shoes
    riley_fewer = 3 # Riley has 3 fewer
    riley_pairs = ellie_pairs - riley_fewer

    # L2
    total_pairs = ellie_pairs + riley_pairs

    # FA
    answer = total_pairs
    return answer
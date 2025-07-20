def solve():
    """Index: 6193.
    Returns: the number of shoes Clinton has.
    """
    # L1
    more_belts_than_hats = 2 # 2 more belts than hats
    num_hats = 5 # 5 hats
    num_belts = more_belts_than_hats + num_hats

    # L2
    multiplier_for_shoes = 2 # twice as many shoes
    num_shoes = multiplier_for_shoes * num_belts

    # FA
    answer = num_shoes
    return answer
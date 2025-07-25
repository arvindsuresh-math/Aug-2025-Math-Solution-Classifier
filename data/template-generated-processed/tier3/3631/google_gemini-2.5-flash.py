def solve():
    """Index: 3631.
    Returns: the number of pairs of shoes Codger needs to buy.
    """
    # L1
    num_sets_desired = 5 # 5 complete 3-piece sets of shoes
    shoes_per_set = 3 # 3-piece set of shoes
    total_shoes_needed = num_sets_desired * shoes_per_set

    # L2
    shoes_owned = 3 # owns the 3-piece set of shoes he is wearing
    additional_shoes_to_buy = total_shoes_needed - shoes_owned

    # L3
    shoes_per_pair = 2 # stores only sell the shoes in pairs
    pairs_to_buy = additional_shoes_to_buy / shoes_per_pair

    # FA
    answer = pairs_to_buy
    return answer
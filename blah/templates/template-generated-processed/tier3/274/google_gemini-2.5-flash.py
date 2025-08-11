def solve():
    """Index: 274.
    Returns: the number of more marbles Mabel has than Amanda.
    """
    # L1
    mabel_marbles = 85 # Mabel has 85 marbles
    mabel_katrina_multiplier = 5 # 5 times as many marbles as Katrina
    katrina_marbles = mabel_marbles / mabel_katrina_multiplier

    # L2
    amanda_katrina_multiplier = 2 # twice as many marbles as Katrina
    twice_katrina_marbles = katrina_marbles * amanda_katrina_multiplier

    # L3
    amanda_needs_more = 12 # needs 12 more marbles
    amanda_marbles = twice_katrina_marbles - amanda_needs_more

    # L4
    mabel_more_than_amanda = mabel_marbles - amanda_marbles

    # FA
    answer = mabel_more_than_amanda
    return answer
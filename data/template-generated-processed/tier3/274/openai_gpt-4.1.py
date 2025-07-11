def solve():
    """Index: 274.
    Returns: how many more marbles Mabel has than Amanda.
    """
    # L1
    mabel_marbles = 85 # Mabel has 85 marbles
    mabel_katrina_ratio = 5 # Mabel has 5 times as many marbles as Katrina
    katrina_marbles = mabel_marbles / mabel_katrina_ratio

    # L2
    twice_katrina = katrina_marbles * 2 # twice as many marbles as Katrina

    # L3
    amanda_needs = 12 # Amanda needs 12 more marbles
    amanda_marbles = twice_katrina - amanda_needs

    # L4
    mabel_amanda_difference = mabel_marbles - amanda_marbles

    # FA
    answer = mabel_amanda_difference
    return answer
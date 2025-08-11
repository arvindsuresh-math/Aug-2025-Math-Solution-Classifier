def solve():
    """Index: 5350.
    Returns: the total number of marbles Katie has.
    """
    # L1
    pink_marbles = 13 # 13 pink marbles
    fewer_orange_than_pink = 9 # 9 fewer orange marbles than pink marbles
    orange_marbles = pink_marbles - fewer_orange_than_pink

    # L2
    times_purple_as_orange = 4 # 4 times as many purple marbles as orange marbles
    purple_marbles = orange_marbles * times_purple_as_orange

    # L3
    total_marbles = pink_marbles + orange_marbles + purple_marbles

    # FA
    answer = total_marbles
    return answer
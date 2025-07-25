def solve():
    """Index: 448.
    Returns: the total number of marbles in all jars.
    """
    # L1
    jar_a = 28 # Jar A has 28 marbles
    jar_b_more_than_a = 12 # Jar B has 12 more marbles than jar A
    jar_b = jar_a + jar_b_more_than_a

    # L2
    jar_c_multiplier = 2 # Jar C has twice as many marbles as jar B
    jar_c = jar_c_multiplier * jar_b

    # L3
    total_marbles = jar_a + jar_b + jar_c

    # FA
    answer = total_marbles
    return answer
def solve():
    """Index: 448.
    Returns: the total number of marbles in all jars.
    """
    # L1
    jar_a_marbles = 28 # Jar A has 28 marbles
    more_than_jar_a = 12 # 12 more marbles than jar A
    jar_b_marbles = jar_a_marbles + more_than_jar_a

    # L2
    multiplier_for_jar_c = 2 # twice as many marbles
    jar_c_marbles = multiplier_for_jar_c * jar_b_marbles

    # L3
    total_marbles = jar_a_marbles + jar_b_marbles + jar_c_marbles

    # FA
    answer = total_marbles
    return answer
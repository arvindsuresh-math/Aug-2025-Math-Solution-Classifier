def solve():
    """Index: 6296.
    Returns: the total number of marbles.
    """
    # L1
    jars = 16 # 16 jars
    twice_factor = 2 # twice the number
    clay_pots = jars / twice_factor

    # L2
    marbles_per_jar = 5 # each jar has 5 marbles
    total_marbles_jars = marbles_per_jar * jars

    # L3
    marbles_factor_clay_pot = 3 # three times as many
    marbles_per_clay_pot = marbles_factor_clay_pot * marbles_per_jar

    # L4
    total_marbles_clay_pots = marbles_per_clay_pot * clay_pots

    # L5
    total_marbles = total_marbles_clay_pots + total_marbles_jars

    # FA
    answer = total_marbles
    return answer
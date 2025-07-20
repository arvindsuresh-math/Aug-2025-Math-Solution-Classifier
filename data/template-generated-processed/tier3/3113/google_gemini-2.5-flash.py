def solve():
    """Index: 3113.
    Returns: the number of jars of pickled mangoes Jordan's sister can make.
    """
    # L1
    total_mangoes = 54 # Jordan picked 54 mangoes
    ripe_fraction_denominator = 3 # One-third of the mangoes
    ripe_mangoes = total_mangoes / ripe_fraction_denominator

    # L2
    unripe_mangoes = total_mangoes - ripe_mangoes

    # L3
    kept_unripe_mangoes = 16 # Jordan kept 16 unripe mangoes
    mangoes_for_sister = unripe_mangoes - kept_unripe_mangoes

    # L4
    mangoes_per_jar = 4 # it takes 4 mangoes to fill a jar
    jars_made = mangoes_for_sister / mangoes_per_jar

    # FA
    answer = jars_made
    return answer
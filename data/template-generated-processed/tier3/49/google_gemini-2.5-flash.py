def solve():
    """Index: 49.
    Returns: the number of shells Alan collected.
    """
    # L1
    laurie_shells = 36 # Laurie collected 36 shells
    ben_fraction_denominator = 3 # a third of what Laurie did
    ben_shells = laurie_shells / ben_fraction_denominator

    # L2
    alan_multiplier = 4 # Alan collected four times as many shells as Ben did
    alan_shells = ben_shells * alan_multiplier

    # FA
    answer = alan_shells
    return answer
def solve(
        alan_multiplier: int = 4, # Alan collected four times as many shells as Ben did
        ben_fraction_denominator: int = 3, # Ben got a late start and only collected a third of what Laurie did
        laurie_shells: int = 36 # Laurie collected 36 shells
    ):
    """Index: 49.
    Returns: the number of shells Alan collected.
    """

    #: L1
    ben_shells = laurie_shells / ben_fraction_denominator # eval: 12.0 = 36 / 3

    #: L2
    alan_shells = ben_shells * alan_multiplier # eval: 48.0 = 12.0 * 4

    #: FA
    answer = alan_shells # eval: 48.0 = 48.0
    return answer # eval: return 48.0

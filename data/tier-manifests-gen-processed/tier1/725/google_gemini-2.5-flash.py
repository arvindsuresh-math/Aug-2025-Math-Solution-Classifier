def solve():
    """Index: 725.
    Returns: the number of toads Sarah has.
    """
    # L1
    tim_toads = 30 # Tim has 30 toads
    jim_more_than_tim = 20 # 20 more toads than Tim
    jim_toads = tim_toads + jim_more_than_tim

    # L2
    sarah_multiplier = 2 # twice as many toads
    sarah_toads = jim_toads * sarah_multiplier

    # FA
    answer = sarah_toads
    return answer
def solve():
    """Index: 725.
    Returns: the number of toads Sarah has.
    """
    # L1
    tim_toads = 30 # Tim has 30 toads
    jim_more_than_tim = 20 # Jim has 20 more toads than Tim does
    jim_toads = tim_toads + jim_more_than_tim

    # L2
    sarah_times_jim = 2 # Sarah has twice as many toads as Jim does
    sarah_toads = jim_toads * sarah_times_jim

    # FA
    answer = sarah_toads
    return answer
def solve():
    """Index: 127.
    Returns: the combined total number of meows the three cats make in 5 minutes.
    """
    # L1
    first_cat_meows_per_minute = 3 # first cat meowed 3 times per minute
    second_cat_multiplier = 2 # second cat meowed twice as frequently as the first cat
    second_cat_meows_per_minute = second_cat_multiplier * first_cat_meows_per_minute

    # L2
    third_cat_divisor = 3 # third cat meowed at one-third the frequency of the second cat
    third_cat_meows_per_minute = second_cat_meows_per_minute / third_cat_divisor

    # L3
    combined_meows_per_minute = first_cat_meows_per_minute + second_cat_meows_per_minute + third_cat_meows_per_minute

    # L4
    minutes = 5 # in 5 minutes
    total_meows = minutes * combined_meows_per_minute

    # FA
    answer = total_meows
    return answer
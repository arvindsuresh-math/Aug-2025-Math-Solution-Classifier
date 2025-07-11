def solve():
    """Index: 127.
    Returns: the combined total number of meows the three cats make.
    """
    # L1
    first_cat_meows_per_minute = 3 # The first cat meowed 3 times per minute
    second_cat_frequency_multiplier = 2 # twice as frequently
    second_cat_meows_per_minute = second_cat_frequency_multiplier * first_cat_meows_per_minute

    # L2
    third_cat_frequency_divisor = 3 # one-third the frequency
    third_cat_meows_per_minute = second_cat_meows_per_minute / third_cat_frequency_divisor

    # L3
    combined_meows_per_minute = first_cat_meows_per_minute + second_cat_meows_per_minute + third_cat_meows_per_minute

    # L4
    time_in_minutes = 5 # in 5 minutes
    total_meows = time_in_minutes * combined_meows_per_minute

    # FA
    answer = total_meows
    return answer
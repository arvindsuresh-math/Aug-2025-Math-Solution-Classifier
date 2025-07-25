def solve():
    """Index: 7287.
    Returns: the difference in candy bars between Lena and Nicole.
    """
    # L1
    lena_current_candy_bars = 16 # Lena has 16 candy bars
    lena_needed_candy_bars = 5 # She needs 5 more candy bars
    kevin_multiplier = 3 # to have 3 times as many as Kevin
    kevin_candy_bars = (lena_current_candy_bars + lena_needed_candy_bars) / kevin_multiplier

    # L2
    nicole_difference = 4 # Kevin has 4 candy bars less than Nicole
    nicole_candy_bars = kevin_candy_bars + nicole_difference

    # L3
    difference_lena_nicole = lena_current_candy_bars - nicole_candy_bars

    # FA
    answer = difference_lena_nicole
    return answer
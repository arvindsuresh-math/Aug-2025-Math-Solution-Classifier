def solve():
    """Index: 2584.
    Returns: the percentage of flyers Belinda passed out.
    """
    # L1
    ryan_flyers = 42 # Ryan passed out 42 flyers
    alyssa_flyers = 67 # Alyssa passed out 67
    scott_flyers = 51 # Scott passed out 51
    friends_total_flyers = ryan_flyers + alyssa_flyers + scott_flyers

    # L2
    total_flyers = 200 # 200 flyers to distribute
    belinda_flyers = total_flyers - friends_total_flyers

    # L3
    belinda_flyers_decimal = belinda_flyers / total_flyers

    # L4
    percent_multiplier = 100 # WK
    belinda_percentage = belinda_flyers_decimal * percent_multiplier

    # FA
    answer = belinda_percentage
    return answer
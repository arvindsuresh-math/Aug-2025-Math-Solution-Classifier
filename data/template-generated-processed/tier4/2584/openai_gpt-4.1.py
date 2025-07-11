def solve():
    """Index: 2584.
    Returns: the percentage of flyers Belinda passed out.
    """
    # L1
    flyers_ryan = 42 # 42 by Ryan
    flyers_alyssa = 67 # 67 by Alyssa
    flyers_scott = 51 # 51 by Scott
    friends_total_flyers = flyers_ryan + flyers_alyssa + flyers_scott

    # L2
    total_flyers = 200 # 200 flyers to distribute
    belinda_flyers = total_flyers - friends_total_flyers

    # L3
    belinda_fraction = belinda_flyers / total_flyers

    # L4
    percent_factor = 100 # WK
    belinda_percent = belinda_fraction * percent_factor

    # FA
    answer = belinda_percent
    return answer
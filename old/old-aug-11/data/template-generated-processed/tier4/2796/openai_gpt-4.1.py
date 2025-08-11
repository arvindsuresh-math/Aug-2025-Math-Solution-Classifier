def solve():
    """Index: 2796.
    Returns: the percentage of Boyd's friends who are boys.
    """
    # L1
    julian_total_friends = 80 # Julian has 80 Facebook friends
    julian_girl_fraction = 0.40 # 40% are girls
    julian_girl_friends = julian_girl_fraction * julian_total_friends

    # L2
    boyd_girl_multiplier = 2 # Boyd has twice as many friends who are girls
    boyd_girl_friends = boyd_girl_multiplier * julian_girl_friends

    # L3
    boyd_total_friends = 100 # Boyd has 100 friends total
    boyd_boy_friends = boyd_total_friends - boyd_girl_friends

    # L4
    percent_multiplier = 100 # WK
    boyd_boy_percent = boyd_boy_friends / boyd_total_friends * percent_multiplier

    # FA
    answer = boyd_boy_percent
    return answer
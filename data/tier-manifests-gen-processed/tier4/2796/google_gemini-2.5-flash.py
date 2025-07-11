def solve():
    """Index: 2796.
    Returns: the percentage of Boyd's friends who are boys.
    """
    # L1
    julian_total_friends = 80 # Julian has 80 Facebook friends
    julian_girls_percent = 0.40 # 40% are girls
    julian_girls_friends = julian_girls_percent * julian_total_friends

    # L2
    boyd_girls_multiplier = 2 # twice as many friends who are girls
    boyd_girls_friends = boyd_girls_multiplier * julian_girls_friends

    # L3
    boyd_total_friends = 100 # has 100 friends total
    boyd_boys_friends = boyd_total_friends - boyd_girls_friends

    # L4
    percentage_multiplier = 100 # WK
    boyd_boys_percentage = boyd_boys_friends / boyd_total_friends * percentage_multiplier

    # FA
    answer = boyd_boys_percentage
    return answer
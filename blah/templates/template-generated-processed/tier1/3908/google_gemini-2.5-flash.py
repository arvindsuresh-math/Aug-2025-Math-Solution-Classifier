def solve():
    """Index: 3908.
    Returns: the total number of times Michael cleans himself in 52 weeks.
    """
    # L1
    bath_per_week = 2 # takes a bath twice a week
    shower_per_week = 1 # a shower once a week
    total_cleans_per_week = bath_per_week + shower_per_week

    # L2
    num_weeks = 52 # in 52 weeks
    total_cleans_in_52_weeks = num_weeks * total_cleans_per_week

    # FA
    answer = total_cleans_in_52_weeks
    return answer
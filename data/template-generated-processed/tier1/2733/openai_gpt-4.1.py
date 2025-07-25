def solve():
    """Index: 2733.
    Returns: the number of ducks in the combined flock after 5 years.
    """
    # L1
    ducks_killed_per_year = 20 # 20 ducks from a flock are killed
    ducks_born_per_year = 30 # another 30 are born
    net_ducks_per_year = ducks_born_per_year - ducks_killed_per_year

    # L2
    years = 5 # after 5 years
    total_ducks_gained = net_ducks_per_year * years

    # L3
    original_flock_size = 100 # original flock size is 100 ducks
    original_flock_after_years = original_flock_size + total_ducks_gained

    # L4
    other_flock_size = 150 # another flock of 150 ducks
    combined_flock = original_flock_after_years + other_flock_size

    # FA
    answer = combined_flock
    return answer
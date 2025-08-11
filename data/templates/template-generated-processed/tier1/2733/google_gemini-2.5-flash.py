def solve():
    """Index: 2733.
    Returns: the number of ducks in the combined flock.
    """
    # L1
    ducks_born_per_year = 30 # 30 are born
    ducks_killed_per_year = 20 # 20 ducks from a flock are killed
    net_gain_per_year = ducks_born_per_year - ducks_killed_per_year

    # L2
    years_passed = 5 # After 5 years
    total_gain_over_years = net_gain_per_year * years_passed

    # L3
    original_flock_size = 100 # original flock size is 100 ducks
    flock_size_after_years = original_flock_size + total_gain_over_years

    # L4
    second_flock_size = 150 # another flock of 150 ducks
    combined_flock_size = flock_size_after_years + second_flock_size

    # FA
    answer = combined_flock_size
    return answer
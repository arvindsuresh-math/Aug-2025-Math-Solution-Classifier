def solve():
    """Index: 5718.
    Returns: the number of slices of bread left from the loaf.
    """
    # L1
    sandwiches_per_day_regular = 1 # made a sandwich for lunch every day
    days_in_week = 7 # WK
    regular_sandwiches_made = sandwiches_per_day_regular * days_in_week

    # L2
    extra_sandwiches_saturday = 1 # made two sandwiches (one extra on Saturday)
    total_sandwiches_made = regular_sandwiches_made + extra_sandwiches_saturday

    # L3
    slices_per_sandwich = 2 # two slices of bread
    total_slices_used = total_sandwiches_made * slices_per_sandwich

    # L4
    initial_loaf_size = 22 # 22-slice loaf
    slices_left = initial_loaf_size - total_slices_used

    # FA
    answer = slices_left
    return answer
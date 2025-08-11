def solve():
    """Index: 6492.
    Returns: the total number of worms 5 crows will eat in 2 hours.
    """
    # L1
    initial_worms = 30 # 30 worms
    initial_crows = 3 # 3 crows
    worms_per_crow_per_hour = initial_worms / initial_crows

    # L2
    new_crows = 5 # 5 crows
    worms_per_hour_for_new_crows = new_crows * worms_per_crow_per_hour

    # L3
    hours = 2 # 2 hours
    total_worms = hours * worms_per_hour_for_new_crows

    # FA
    answer = total_worms
    return answer
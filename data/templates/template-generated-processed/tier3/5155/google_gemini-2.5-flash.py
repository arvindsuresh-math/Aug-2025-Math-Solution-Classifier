def solve():
    """Index: 5155.
    Returns: the total number of pieces of cutlery in the drawer.
    """
    # L1
    forks = 6 # 6 forks
    more_knives_than_forks = 9 # 9 more knives than forks
    knives = forks + more_knives_than_forks

    # L2
    twice_multiplier = 2 # twice as many spoons
    spoons = knives * twice_multiplier

    # L3
    half_divisor = 2 # half as many teaspoons
    teaspoons = forks / half_divisor

    # L4
    initial_total_cutlery = forks + knives + spoons + teaspoons

    # L5
    added_per_type = 2 # 2 of each cutlery is added
    num_cutlery_types = 4 # 4 types of cutlery
    total_added_cutlery = added_per_type * num_cutlery_types

    # L6
    final_total_cutlery = initial_total_cutlery + total_added_cutlery

    # FA
    answer = final_total_cutlery
    return answer
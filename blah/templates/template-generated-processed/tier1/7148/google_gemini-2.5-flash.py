def solve():
    """Index: 7148.
    Returns: the total number of koi fish in the tank after three weeks.
    """
    # L1
    num_weeks = 3 # Over the next 3 weeks
    days_per_week = 7 # WK
    total_days = num_weeks * days_per_week

    # L2
    koi_added_per_day = 2 # added 2 koi fish
    total_koi_added = total_days * koi_added_per_day

    # L3
    goldfish_added_per_day = 5 # and 5 goldfish per day
    total_goldfish_added = goldfish_added_per_day * total_days

    # L4
    initial_total_fish = 280 # total of 280 fish
    final_total_fish = initial_total_fish + total_koi_added + total_goldfish_added

    # L5
    final_goldfish = 200 # had 200 goldfish at the end of the three weeks
    final_koi_fish = final_total_fish - final_goldfish

    # FA
    answer = final_koi_fish
    return answer
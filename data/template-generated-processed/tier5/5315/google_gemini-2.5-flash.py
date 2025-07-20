def solve():
    """Index: 5315.
    Returns: the distance of Sam's morning run.
    """
    # L3
    total_distance_all_day = 18 # 18 miles in all
    bike_ride_distance = 12 # biked for 12 miles
    walk_and_run_total = total_distance_all_day - bike_ride_distance

    # L4
    run_coefficient_val = 1 # From "X" in "X + 2X"
    walk_multiplier_val = 2 # From "2X" in "X + 2X"
    combined_coefficient = run_coefficient_val + walk_multiplier_val

    # L5
    run_distance = walk_and_run_total / combined_coefficient

    # FA
    answer = run_distance
    return answer
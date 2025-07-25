def solve():
    """Index: 6297.
    Returns: Jordan's current weight after his exercise program.
    """
    # L1
    pounds_lost_per_week_phase1 = 3 # loses 3 pounds a week
    weeks_phase1 = 4 # for the first 4 weeks
    total_lost_phase1 = pounds_lost_per_week_phase1 * weeks_phase1

    # L2
    pounds_lost_per_week_phase2 = 2 # loses 2 pounds a week
    weeks_phase2 = 8 # for 8 weeks
    total_lost_phase2 = pounds_lost_per_week_phase2 * weeks_phase2

    # L3
    total_pounds_lost = total_lost_phase1 + total_lost_phase2

    # L4
    initial_weight = 250 # weighs 250 pounds
    current_weight = initial_weight - total_pounds_lost

    # FA
    answer = current_weight
    return answer
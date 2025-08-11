def solve():
    """Index: 789.
    Returns: the total number of days until James can lift heavy again.
    """
    # L1
    pain_subsided_days = 3 # pain subsided after 3 days
    healing_multiplier = 5 # at least 5 times that long to fully heal
    healing_days = pain_subsided_days * healing_multiplier

    # L2
    wait_after_healing = 3 # wait another 3 days before he started working out again
    start_exercising_days = healing_days + wait_after_healing

    # L3
    wait_weeks = 3 # wait 3 weeks after that to start lifting heavy again
    days_per_week = 7 # WK
    wait_heavy_days = wait_weeks * days_per_week

    # L4
    total_days = start_exercising_days + wait_heavy_days

    # FA
    answer = total_days
    return answer
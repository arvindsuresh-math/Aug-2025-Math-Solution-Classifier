def solve():
    """Index: 789.
    Returns: the total number of days until James can lift heavy again.
    """
    # L1
    pain_subsided_days = 3 # pain subsided after 3 days
    healing_multiplier = 5 # 5 times that long
    healing_days = pain_subsided_days * healing_multiplier

    # L2
    wait_before_exercising = 3 # wait another 3 days before he started working out again
    days_to_start_exercising = healing_days + wait_before_exercising

    # L3
    wait_weeks_for_lifting = 3 # wait 3 weeks after that
    days_per_week = 7 # WK
    days_to_wait_for_lifting = wait_weeks_for_lifting * days_per_week

    # L4
    total_wait_days = days_to_start_exercising + days_to_wait_for_lifting

    # FA
    answer = total_wait_days
    return answer
def solve():
    """Index: 4430.
    Returns: the number of additional weeks Barbara needs to save.
    """
    # L1
    watch_cost = 100 # wristwatch that costs $100
    current_savings = 20 # currently only has $20
    remaining_to_save = watch_cost - current_savings

    # L2
    weekly_allowance = 5 # allowance of $5 a week
    weeks_needed = remaining_to_save / weekly_allowance

    # FA
    answer = weeks_needed
    return answer
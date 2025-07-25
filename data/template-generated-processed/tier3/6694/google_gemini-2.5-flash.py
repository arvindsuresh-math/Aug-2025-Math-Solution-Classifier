def solve():
    """Index: 6694.
    Returns: the number of additional days John must work.
    """
    # L1
    total_made = 250 # So far, he's made $250
    days_worked_initial = 10 # 10 days ago
    daily_earnings = total_made / days_worked_initial

    # L2
    double_multiplier = 2 # twice this amount
    target_amount = total_made * double_multiplier

    # L3
    total_days_needed = target_amount / daily_earnings

    # L4
    additional_days_needed = total_days_needed - days_worked_initial

    # FA
    answer = additional_days_needed
    return answer
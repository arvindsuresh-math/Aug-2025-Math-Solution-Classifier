def solve():
    """Index: 2550.
    Returns: the number of hours Nancy has to work.
    """
    # L1
    total_earnings_L1 = 28 # Nancy earns $28
    hours_worked_L1 = 4 # working 4 hours
    earnings_per_hour = total_earnings_L1 / hours_worked_L1

    # L2
    target_earnings = 70 # earn $70
    hours_to_work = target_earnings / earnings_per_hour

    # FA
    answer = hours_to_work
    return answer
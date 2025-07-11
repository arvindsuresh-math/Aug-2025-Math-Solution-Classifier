def solve():
    """Index: 2539.
    Returns: the percentage of the money they planned to spend that they saved.
    """
    # L1
    num_passengers = 4 # A family of 4 arrives
    cost_per_orange = 1.5 # oranges would've cost $1.5 each
    cost_of_oranges = num_passengers * cost_per_orange

    # L2
    planned_spending = 15 # spend $15 in total
    proportion_saved = cost_of_oranges / planned_spending

    # L3
    percent_multiplier = 100 # WK
    percentage_saved = proportion_saved * percent_multiplier

    # FA
    answer = percentage_saved
    return answer
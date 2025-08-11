def solve():
    """Index: 2539.
    Returns: the percentage of the money the family planned to spend that they saved instead.
    """
    # L1
    num_passengers = 4 # family of 4 arrives
    orange_price = 1.5 # oranges would've cost $1.5 each
    oranges_cost = num_passengers * orange_price

    # L2
    planned_spending = 15 # they would spend $15 in total
    proportion_saved = oranges_cost / planned_spending

    # L3
    percent_factor = 100 # WK
    percent_saved = proportion_saved * percent_factor

    # FA
    answer = percent_saved
    return answer
def solve():
    """Index: 4759.
    Returns: the cost of the new barbell.
    """
    # L1
    old_barbell_cost = 250 # old $250 barbell
    increase_percent_decimal = 0.3 # 30% more
    cost_increase = old_barbell_cost * increase_percent_decimal

    # L2
    new_barbell_cost = old_barbell_cost + cost_increase

    # FA
    answer = new_barbell_cost
    return answer
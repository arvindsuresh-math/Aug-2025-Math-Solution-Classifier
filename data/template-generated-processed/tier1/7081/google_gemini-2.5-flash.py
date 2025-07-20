def solve():
    """Index: 7081.
    Returns: the money remaining in the teacher's budget after purchasing school supplies.
    """
    # L1
    remaining_budget_last_year = 6 # $6 budget from last year
    budget_this_year = 50 # $50 budget
    total_budget = remaining_budget_last_year + budget_this_year

    # L2
    cost_supply_1 = 13 # $13
    cost_supply_2 = 24 # $24
    total_expenses = cost_supply_1 + cost_supply_2

    # L3
    remaining_budget = total_budget - total_expenses

    # FA
    answer = remaining_budget
    return answer
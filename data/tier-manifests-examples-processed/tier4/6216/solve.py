def solve():
    """Index: 6216.
    Returns: the number of softballs they can buy with the new budget.
    """
    # L1
    num_dodgeballs = 15 # 15 dodgeballs
    dodgeball_cost = 5 # for $5 each
    old_budget = num_dodgeballs * dodgeball_cost

    # L2
    budget_increase_percent = 0.2 # add 20% to the gym budget
    budget_increase_amount = old_budget * budget_increase_percent

    # L3
    new_budget = old_budget + budget_increase_amount

    # L4
    softball_cost = 9 # softballs instead, which cost $9 each
    num_softballs = new_budget / softball_cost

    # FA
    answer = num_softballs
    return answer
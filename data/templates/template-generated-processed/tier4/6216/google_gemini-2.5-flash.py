def solve():
    """Index: 6216.
    Returns: the number of softballs that can be bought with the new budget.
    """
    # L1
    num_dodgeballs_old_budget = 15 # 15 dodgeballs
    cost_per_dodgeball = 5 # $5 each
    old_budget = num_dodgeballs_old_budget * cost_per_dodgeball

    # L2
    budget_increase_percent = 0.2 # add 20%
    budget_increase_amount = old_budget * budget_increase_percent

    # L3
    new_budget = old_budget + budget_increase_amount

    # L4
    cost_per_softball = 9 # $9 each
    num_softballs = new_budget / cost_per_softball

    # FA
    answer = num_softballs
    return answer
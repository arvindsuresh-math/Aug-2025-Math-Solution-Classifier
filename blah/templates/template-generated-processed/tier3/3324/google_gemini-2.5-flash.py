def solve():
    """Index: 3324.
    Returns: the amount of money Monica and Sheila each need to add.
    """
    # L1
    toilet_paper_cost = 12 # The toilet paper cost $12
    groceries_multiplier = 2 # twice the cost of the toilet paper
    groceries_cost = toilet_paper_cost * groceries_multiplier

    # L2
    total_spent_initial = toilet_paper_cost + groceries_cost

    # L3
    initial_money = 50 # Their mother gave them $50
    money_left_after_groceries = initial_money - total_spent_initial

    # L4
    boots_cost_multiplier = 3 # 3 times the amount they had left
    cost_per_pair_boots = money_left_after_groceries * boots_cost_multiplier

    # L5
    num_pairs_boots = 2 # two pairs of boots
    total_cost_two_pairs_boots = cost_per_pair_boots * num_pairs_boots

    # L6
    additional_money_needed = total_cost_two_pairs_boots - money_left_after_groceries

    # L7
    num_twins = 2 # Monica and Sheila are twins
    money_per_twin = additional_money_needed / num_twins

    # FA
    answer = money_per_twin
    return answer
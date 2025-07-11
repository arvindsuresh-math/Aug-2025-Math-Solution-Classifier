def solve():
    """Index: 2418.
    Returns: the amount of money left on Lyra's weekly budget.
    """
    # L1
    cost_per_pound_beef = 3 # $3 per pound
    pounds_of_beef = 5 # 5 pounds of beef
    cost_of_beef = cost_per_pound_beef * pounds_of_beef

    # L2
    cost_fried_chicken = 12 # 1 bucket of fried chicken that costs $12
    total_spent = cost_fried_chicken + cost_of_beef

    # L3
    weekly_budget = 80 # $80 budget for a week
    remaining_budget = weekly_budget - total_spent

    # FA
    answer = remaining_budget
    return answer
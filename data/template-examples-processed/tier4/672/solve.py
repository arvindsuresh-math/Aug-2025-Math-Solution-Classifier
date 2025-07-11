def solve():
    """Index: 672.
    Returns: the amount Harris will spend on carrots in one year.
    """
    # L1
    carrots_per_day = 1 # 1 large organic carrot
    days_per_year = 365 # WK
    carrots_per_year = carrots_per_day * days_per_year

    # L2
    carrots_per_bag = 5 # 5 carrots in a 1 pound bag
    bags_needed = carrots_per_year / carrots_per_bag

    # L3
    cost_per_bag = 2.00 # each bag costs $2.00
    total_cost = cost_per_bag * bags_needed

    # FA
    answer = total_cost
    return answer
def solve():
    """Index: 1483.
    Returns: the amount of money Mia spent on each parent's gift.
    """
    # L1
    cost_per_sibling = 30 # spent $30 on each of her 3 siblings
    num_siblings = 3 # 3 siblings
    spent_on_siblings = cost_per_sibling * num_siblings

    # L2
    total_spending = 150 # spent a total of $150 on Christmas gifts
    spent_on_parents = total_spending - spent_on_siblings

    # L3
    num_parents = 2 # each of her parents received gifts of equal value
    cost_per_parent_gift = spent_on_parents / num_parents

    # FA
    answer = cost_per_parent_gift
    return answer
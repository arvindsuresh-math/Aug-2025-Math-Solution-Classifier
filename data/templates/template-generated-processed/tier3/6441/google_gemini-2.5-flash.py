def solve():
    """Index: 6441.
    Returns: Jaco's budget for each of his mother and father's gift.
    """
    # L1
    gift_cost_per_friend = 9 # worth $9 each
    num_friends = 8 # his 8 friends
    total_cost_friends_gifts = gift_cost_per_friend * num_friends

    # L2
    total_budget = 100 # a $100 budget
    remaining_budget = total_budget - total_cost_friends_gifts

    # L3
    num_parents = 2 # mother and father
    budget_per_parent_gift = remaining_budget / num_parents

    # FA
    answer = budget_per_parent_gift
    return answer
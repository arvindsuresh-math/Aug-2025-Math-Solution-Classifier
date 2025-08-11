def solve():
    """Index: 4622.
    Returns: the cost of a single figurine in dollars.
    """
    # L1
    num_televisions = 5 # bought 5 televisions
    cost_per_television = 50 # each cost $50
    cost_televisions = num_televisions * cost_per_television

    # L2
    total_spent = 260 # spent $260 in total
    remaining_money = total_spent - cost_televisions

    # L3
    num_figurines = 10 # purchased 10 figurines
    cost_per_figurine = remaining_money / num_figurines

    # FA
    answer = cost_per_figurine
    return answer
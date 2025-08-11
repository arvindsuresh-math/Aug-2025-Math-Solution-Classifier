def solve():
    """Index: 5295.
    Returns: the amount of change Jack gets.
    """
    # L1
    num_sandwiches = 3 # 3 sandwiches
    cost_per_sandwich = 5 # $5 each
    total_cost = num_sandwiches * cost_per_sandwich

    # L2
    bill_paid = 20 # $20 bill
    change = bill_paid - total_cost

    # FA
    answer = change
    return answer
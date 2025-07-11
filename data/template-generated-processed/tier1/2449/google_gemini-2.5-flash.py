def solve():
    """Index: 2449.
    Returns: the amount of change Yanna got back.
    """
    # L1
    num_shirts = 10 # ten shirts
    cost_per_shirt = 5 # $5 each
    cost_shirts = num_shirts * cost_per_shirt

    # L2
    num_sandals = 3 # three pairs of sandals
    cost_per_sandal = 3 # $3 each
    cost_sandals = num_sandals * cost_per_sandal

    # L3
    total_spent = cost_shirts + cost_sandals

    # L4
    bill_given = 100 # a one hundred dollar bill
    change_back = bill_given - total_spent

    # FA
    answer = change_back
    return answer
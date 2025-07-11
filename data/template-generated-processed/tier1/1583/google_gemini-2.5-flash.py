def solve():
    """Index: 1583.
    Returns: the amount of money saved by picking the cheaper computer option.
    """
    # L1
    cost_per_used_computer = 200 # $200 each
    num_used_computers = 2 # 2 used computers
    total_cost_used_computers = cost_per_used_computer * num_used_computers

    # L2
    cost_new_computer = 600 # $600
    savings = cost_new_computer - total_cost_used_computers

    # FA
    answer = savings
    return answer
def solve():
    """Index: 1583.
    Returns: the amount of money James will save by picking the cheaper computer option.
    """
    # L1
    used_computer_cost = 200 # $200 each
    num_used_computers = 2 # 2 used computers
    total_used_cost = used_computer_cost * num_used_computers

    # L2
    new_computer_cost = 600 # $600 for new computer
    savings = new_computer_cost - total_used_cost

    # FA
    answer = savings
    return answer
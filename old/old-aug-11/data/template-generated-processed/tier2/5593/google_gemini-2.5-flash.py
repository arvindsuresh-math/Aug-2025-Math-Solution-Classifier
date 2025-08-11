def solve():
    """Index: 5593.
    Returns: how much more money it will cost to complete the project after inflation.
    """
    # L1
    initial_lumber_cost = 450 # lumber cost $450
    initial_nails_cost = 30 # nails cost $30
    initial_fabric_cost = 80 # fabric cost $80
    initial_total_cost = initial_lumber_cost + initial_nails_cost + initial_fabric_cost

    # L2
    lumber_increase_factor = 1.20 # price of lumber to increase by 20%
    new_lumber_cost = initial_lumber_cost * lumber_increase_factor

    # L3
    nails_increase_factor = 1.10 # price of nails to increase by 10%
    new_nails_cost = initial_nails_cost * nails_increase_factor

    # L4
    fabric_increase_factor = 1.05 # price of fabric to increase by 5%
    new_fabric_cost = initial_fabric_cost * fabric_increase_factor

    # L5
    new_total_cost = new_lumber_cost + new_nails_cost + new_fabric_cost

    # L6
    cost_increase = new_total_cost - initial_total_cost

    # FA
    answer = cost_increase
    return answer
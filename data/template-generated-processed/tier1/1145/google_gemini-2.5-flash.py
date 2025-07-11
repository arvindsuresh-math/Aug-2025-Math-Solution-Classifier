def solve():
    """Index: 1145.
    Returns: the amount of money Daria needs to earn.
    """
    # L1
    daria_ticket = 1 # for her
    num_friends = 3 # three of her friends
    total_people = daria_ticket + num_friends
    cost_per_ticket = 90 # $90
    total_cost = total_people * cost_per_ticket

    # L2
    money_daria_has = 189 # currently has only $189
    money_needed = total_cost - money_daria_has

    # FA
    answer = money_needed
    return answer
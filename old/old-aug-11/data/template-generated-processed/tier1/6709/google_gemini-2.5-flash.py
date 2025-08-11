def solve():
    """Index: 6709.
    Returns: the amount of money Rita has now.
    """
    # L1
    num_dresses = 5 # 5 short dresses
    cost_per_dress = 20 # The dresses cost $20 each
    cost_dresses = num_dresses * cost_per_dress

    # L2
    num_pants = 3 # 3 pairs of pants
    cost_per_pant = 12 # the pants cost $12
    cost_pants = num_pants * cost_per_pant

    # L3
    num_jackets = 4 # 4 jackets
    cost_per_jacket = 30 # the jackets cost $30 each
    cost_jackets = num_jackets * cost_per_jacket

    # L4
    transportation_cost = 5 # spent an additional $5 on transportation
    total_spent = transportation_cost + cost_dresses + cost_pants + cost_jackets

    # L5
    initial_money = 400 # If she had $400 initially
    money_remaining = initial_money - total_spent

    # FA
    answer = money_remaining
    return answer
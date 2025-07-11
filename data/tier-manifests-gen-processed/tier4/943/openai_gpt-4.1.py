def solve():
    """Index: 943.
    Returns: the number of dozen donuts Javier needs to buy and sell to reach his goal.
    """
    # L1
    dozen_size = 12 # WK
    cost_per_dozen = 2.4 # buys each dozen donuts for $2.40
    cost_per_donut = cost_per_dozen / dozen_size

    # L2
    sell_price_per_donut = 1 # sells each donut for $1
    profit_per_donut = sell_price_per_donut - cost_per_donut

    # L3
    goal_amount = 96 # wants to raise $96
    donuts_needed = goal_amount / profit_per_donut

    # L4
    dozens_needed = donuts_needed / dozen_size

    # FA
    answer = dozens_needed
    return answer
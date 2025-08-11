def solve():
    """Index: 6068.
    Returns: the amount of money Tabitha has left.
    """
    # L1
    initial_money = 25 # 25 dollars
    money_to_mom = 8 # gives her mom 8 dollars
    money_after_mom = initial_money - money_to_mom

    # L2
    investment_divisor = 2 # half what is left
    money_after_investment = money_after_mom / investment_divisor

    # L3
    num_items = 5 # 5 items
    cost_per_item = 0.5 # 50 cents each
    total_item_cost = num_items * cost_per_item

    # L4
    money_left = money_after_investment - total_item_cost

    # FA
    answer = money_left
    return answer
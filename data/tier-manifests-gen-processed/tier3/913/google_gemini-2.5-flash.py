def solve():
    """Index: 913.
    Returns: the amount of money the trader made above her goal.
    """
    # L1
    total_profit = 960 # $960 after a week of sales
    split_divisor = 2 # splits the profit in half
    half_profit = total_profit / split_divisor

    # L2
    total_donation = 310 # received a total donation of $310
    total_money_after_donation = total_donation + half_profit

    # L3
    goal_amount = 610 # raise $610 to pay for her next shipment
    money_above_goal = total_money_after_donation - goal_amount

    # FA
    answer = money_above_goal
    return answer
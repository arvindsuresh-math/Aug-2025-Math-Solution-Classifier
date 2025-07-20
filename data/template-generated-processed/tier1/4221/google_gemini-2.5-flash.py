def solve():
    """Index: 4221.
    Returns: the amount of money John has left.
    """
    # L1
    roast_cost = 17 # buys a roast for €17
    vegetables_cost = 11 # vegetables for €11
    total_spent = roast_cost + vegetables_cost

    # L2
    initial_money = 100 # goes to the market with €100
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer
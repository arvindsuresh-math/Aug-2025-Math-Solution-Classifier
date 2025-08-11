def solve():
    """Index: 86.
    Returns: the number of ounces of soda Peter bought.
    """
    # L1
    money_brought = 2 # brought $2 with him
    money_left = 0.50 # leaves with $.50
    money_spent = money_brought - money_left

    # L2
    cost_per_ounce = 0.25 # costs $.25 an ounce
    ounces_bought = money_spent / cost_per_ounce

    # FA
    answer = ounces_bought
    return answer
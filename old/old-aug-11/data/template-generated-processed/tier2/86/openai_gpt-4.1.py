def solve():
    """Index: 86.
    Returns: the number of ounces of soda Peter bought.
    """
    # L1
    money_brought = 2 # He brought $2 with him
    money_left = 0.5 # leaves with $.50
    money_spent = money_brought - money_left

    # L2
    soda_cost_per_ounce = 0.25 # The soda costs $.25 an ounce
    ounces_bought = money_spent / soda_cost_per_ounce

    # FA
    answer = ounces_bought
    return answer
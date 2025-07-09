def solve(
    soda_cost_per_ounce: float = 0.25, # The soda costs $.25 an ounce
    money_brought: float = 2.0, # He brought $2 with him
    money_left: float = 0.50 # leaves with $.50
):
    """Index: 86.
    Returns: the number of ounces of soda Peter bought.
    """

    #: L1
    money_spent = money_brought + money_left # eval: 2.5 = 2.0 + 0.5

    #: L2
    ounces_bought = money_spent / soda_cost_per_ounce # eval: 10.0 = 2.5 / 0.25

    #: FA
    answer = ounces_bought
    return answer # eval: return 10.0

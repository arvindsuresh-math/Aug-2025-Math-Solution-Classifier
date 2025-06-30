def solve(
    money_brought: float = 2.0, # He brought $2 with him
    money_left: float = 0.50, # and leaves with $.50
    cost_per_ounce: float = 0.25 # The soda costs $.25 an ounce
):
    """Index: 86.
    Returns: the number of ounces of soda Peter bought.
    """

    #: L1
    money_spent = money_brought - money_left # eval: 1.5 = 2.0 - 0.5

    #: L2
    ounces_bought = money_spent / cost_per_ounce # eval: 6.0 = 1.5 / 0.25

    #: FA
    answer = ounces_bought # eval: 6.0 = 6.0
    return answer # eval: return 6.0

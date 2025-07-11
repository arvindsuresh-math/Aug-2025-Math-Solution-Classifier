def solve(
    money_brought: float = 2.0,  # Peter brought $2 with him
    money_left: float = 0.5,     # and leaves with $0.50
    cost_per_ounce: float = 0.25 # The soda costs $0.25 an ounce
):
    """Index: 86.
    Returns: the number of ounces of soda Peter bought.
    """
    #: L1
    money_spent = money_brought - money_left

    #: L2
    ounces_bought = money_spent / cost_per_ounce

    answer = ounces_bought  # FINAL ANSWER
    return answer
def solve(
    wallet_cost: int = 100, # which costs $100
    fraction_money_has: float = 1/2, # Betty has only half of the money she needs
    parents_gift: int = 15, # Her parents decided to give her $15
    grandparents_gift_multiplier: int = 2 # her grandparents twice as much as her parents
):
    """Index: 2.
    Returns: the amount of money Betty still needs to buy the wallet.
    """

    #: L1
    initial_money = wallet_cost * fraction_money_has

    #: L2
    grandparents_gift = parents_gift * grandparents_gift_multiplier

    #: L3

    #: FA
    answer = wallet_cost
    return answer
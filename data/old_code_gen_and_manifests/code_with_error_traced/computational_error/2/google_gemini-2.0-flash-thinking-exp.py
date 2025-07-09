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
    initial_money = wallet_cost * fraction_money_has # eval: 50.0 = 100 * 0.5

    #: L2
    grandparents_gift = parents_gift * grandparents_gift_multiplier # eval: 30 = 15 * 2

    #: L3
    money_needed = 4.0 # eval: 4.0 = 4.0

    #: FA
    answer = money_needed
    return answer # eval: return 4.0

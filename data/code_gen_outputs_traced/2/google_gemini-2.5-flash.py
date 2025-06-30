def solve(
        wallet_cost: int = 100, # new wallet which costs $100
        initial_fraction_has: float = 0.5, # Betty has only half of the money she needs
        money_from_parents: int = 15, # Her parents decided to give her $15
        grandparents_multiplier: int = 2 # her grandparents twice as much as her parents
    ):
    """Index: 2.
    Returns: the amount of money Betty still needs to buy the wallet.
    """

    #: L1
    initial_money_betty_has = wallet_cost * initial_fraction_has # eval: 50.0 = 100 * 0.5

    #: L2
    money_from_grandparents = money_from_parents * grandparents_multiplier # eval: 30 = 15 * 2

    #: L3
    money_needed = wallet_cost - initial_money_betty_has - money_from_grandparents - money_from_parents # eval: 5.0 = 100 - 50.0 - 30 - 15

    #: FA
    answer = money_needed
    return answer # eval: return 5.0

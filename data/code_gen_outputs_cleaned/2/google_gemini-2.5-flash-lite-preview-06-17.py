def solve(
    wallet_cost: int = 100, # Betty is saving money for a new wallet which costs $100.
    betty_has_fraction: float = 0.5, # Betty has only half of the money she needs.
    parents_gift: int = 15, # Her parents decided to give her $15 for that purpose
    grandparents_gift_multiplier: int = 2 # her grandparents twice as much as her parents.
):
    """Index: 2.
    Returns: the amount of money Betty still needs to buy the wallet.
    """
    #: L1
    betty_has = wallet_cost * betty_has_fraction

    #: L2
    grandparents_gift = parents_gift * grandparents_gift_multiplier

    #: L3
    money_needed = wallet_cost - betty_has - parents_gift - grandparents_gift

    answer = money_needed # FINAL ANSWER
    return answer
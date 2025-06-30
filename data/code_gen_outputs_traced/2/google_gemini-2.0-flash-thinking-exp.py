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
    money_needed = wallet_cost - initial_money - parents_gift - grandparents_gift # eval: 5.0 = 100 - 50.0 - 15 - 30
    answer = money_needed # FINAL ANSWER # eval: 5.0 = 5.0 # FINAL ANSWER
    return answer # eval: return 5.0
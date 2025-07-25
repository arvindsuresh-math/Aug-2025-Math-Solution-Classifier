def solve():
    """Index: 2.
    Returns: the additional amount of money Betty needs to buy the wallet.
    """
    # L1
    wallet_cost = 100 # wallet which costs $100
    initial_fraction_denominator = 2 # only half of the money she needs
    betty_initial_money = wallet_cost / initial_fraction_denominator

    # L2
    parents_gift = 15 # her parents decided to give her $15
    grandparents_multiplier = 2 # grandparents twice as much as her parents
    grandparents_gift = parents_gift * grandparents_multiplier

    # L3
    answer = wallet_cost - betty_initial_money - grandparents_gift - parents_gift
    # FA
    return answer
def solve():
    """Index: 2.
    Returns: the amount of money Betty still needs to buy the wallet.
    """
    # L1
    wallet_cost = 100 # wallet which costs $100
    initial_fraction_denominator = 2 # half of the money she needs
    initial_money = wallet_cost / initial_fraction_denominator

    # L2
    parents_gift = 15 # her parents decided to give her $15
    grandparents_multiplier = 2 # twice as much as her parents
    grandparents_gift = parents_gift * grandparents_multiplier

    # L3
    money_needed = wallet_cost - initial_money - grandparents_gift - parents_gift

    # FA
    answer = money_needed
    return answer
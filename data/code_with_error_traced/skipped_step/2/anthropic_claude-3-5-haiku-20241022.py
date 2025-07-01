def solve(
    wallet_cost: int = 100,  # wallet costs $100
    betty_savings_fraction: float = 1/2,  # Betty has only half of the money she needs
    parents_contribution: int = 15,  # her parents decided to give her $15
    grandparents_multiplier: int = 2  # her grandparents gave twice as much as her parents
):
    """Index: 2.
    Returns: the amount of money Betty still needs to buy the wallet.
    """

    #: L1
    betty_savings = wallet_cost * betty_savings_fraction # eval: 50.0 = 100 * 0.5

    #: L2
    grandparents_contribution = parents_contribution * grandparents_multiplier # eval: 30 = 15 * 2

    #: L3

    #: FA
    answer = wallet_cost
    return answer # eval: return 100

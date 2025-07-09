def solve(
    wallet_cost: int = 100,  # wallet costs $100
    parents_gift: int = 15   # parents give $15
):
    """Index: 2.
    Returns: the additional amount of money Betty needs to buy the wallet.
    """

    #: L1
    betty_initial = wallet_cost / 2

    #: L2
    grandparents_gift = parents_gift * 2

    #: L3
    money_needed = wallet_cost - betty_initial - grandparents_gift - parents_gift

    #: FA
    answer = money_needed
    return answer
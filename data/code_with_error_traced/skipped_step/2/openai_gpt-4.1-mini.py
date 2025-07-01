def solve(
    wallet_cost: int = 100,  # wallet costs $100
    parents_gift: int = 15   # parents give $15
):
    """Index: 2.
    Returns: the additional amount of money Betty needs to buy the wallet.
    """

    #: L1

    #: L2
    grandparents_gift = parents_gift * 2 # eval: 30 = 15 * 2

    #: L3
    money_needed = wallet_cost - parents_gift - grandparents_gift - parents_gift # eval: 40 = 100 - 15 - 30 - 15

    #: FA
    answer = money_needed
    return answer # eval: return 40

def solve(
    total_earned: int = 28,  # Leah earned $28 working odd jobs
):
    """Index: 54.
    Returns: the amount of money Leah lost after her dog shredded her wallet.
    """

    #: L1
    spent_on_milkshake = total_earned / 7 # eval: 4.0 = 28 / 7

    #: L2
    money_left = total_earned - spent_on_milkshake # eval: 24.0 = 28 - 4.0

    #: L3
    money_in_wallet = 13.0 # eval: 13.0 = 13.0

    #: L4
    money_lost = money_in_wallet - 1 # eval: 12.0 = 13.0 - 1

    #: FA
    answer = money_lost
    return answer # eval: return 12.0

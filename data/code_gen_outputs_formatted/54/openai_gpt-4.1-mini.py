def solve(
    total_earned: int = 28,  # Leah earned $28 working odd jobs
):
    """Index: 54.
    Returns: the amount of money Leah lost after her dog shredded her wallet.
    """

    #: L1
    spent_on_milkshake = total_earned / 7

    #: L2
    money_left = total_earned - spent_on_milkshake

    #: L3
    money_in_wallet = money_left / 2

    #: L4
    money_lost = money_in_wallet - 1

    #: FA
    answer = money_lost
    return answer
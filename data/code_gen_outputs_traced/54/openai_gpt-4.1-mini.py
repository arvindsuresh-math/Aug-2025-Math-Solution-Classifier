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
    money_in_wallet = money_left / 2 # eval: 12.0 = 24.0 / 2

    #: L4
    money_lost = money_in_wallet - 1 # eval: 11.0 = 12.0 - 1

    #: FA
    answer = money_lost # eval: 11.0 = 11.0
    return answer # eval: return 11.0

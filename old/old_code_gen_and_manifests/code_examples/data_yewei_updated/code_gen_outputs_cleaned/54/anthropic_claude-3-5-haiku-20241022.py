def solve(total_earnings: float = 28.0):  # "Leah earned $28 working odd jobs around the neighborhood"
    """
    Index: 54.
    Returns: the amount of money Leah lost when her dog shredded her wallet.
    """
    #: L1 Calculate money spent on milkshake
    milkshake_cost = total_earnings / 7

    #: L2 Calculate remaining money after milkshake
    remaining_after_milkshake = total_earnings - milkshake_cost

    #: L3 Calculate money in wallet
    wallet_money = remaining_after_milkshake / 2

    #: L4 Calculate money lost
    money_lost = wallet_money - 1  # dog left $1 in wallet

    answer = money_lost  # FINAL ANSWER
    return answer
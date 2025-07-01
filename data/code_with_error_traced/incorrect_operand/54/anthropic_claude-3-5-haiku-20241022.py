def solve(
    total_earnings: int = 28,  # Leah earned $28 working odd jobs
    milkshake_fraction: int = 7,  # she spent a seventh of it on a milkshake
    savings_fraction: int = 2,  # she put half of the rest in her savings account
    money_left_unshredded: int = 1  # her dog left $1 unshredded
):
    """Index: 54.
    Returns: the number of dollars Leah lost when her dog shredded her wallet."""

    #: L1
    milkshake_cost = money_left_unshredded / milkshake_fraction # eval: 0.14285714285714285 = 1 / 7

    #: L2
    money_after_milkshake = total_earnings - milkshake_cost # eval: 27.857142857142858 = 28 - 0.14285714285714285

    #: L3
    money_in_wallet = money_after_milkshake / savings_fraction # eval: 13.928571428571429 = 27.857142857142858 / 2

    #: L4
    money_lost = money_in_wallet - money_left_unshredded # eval: 12.928571428571429 = 13.928571428571429 - 1

    #: FA
    answer = money_lost
    return answer # eval: return 12.928571428571429

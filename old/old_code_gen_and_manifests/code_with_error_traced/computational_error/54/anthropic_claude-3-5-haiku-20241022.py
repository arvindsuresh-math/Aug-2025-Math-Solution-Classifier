def solve(
    total_earnings: int = 28,  # Leah earned $28 working odd jobs
    milkshake_fraction: int = 7,  # she spent a seventh of it on a milkshake
    savings_fraction: int = 2,  # she put half of the rest in her savings account
    money_left_unshredded: int = 1  # her dog left $1 unshredded
):
    """Index: 54.
    Returns: the number of dollars Leah lost when her dog shredded her wallet."""

    #: L1
    milkshake_cost = -6.0 # eval: -6.0 = -6.0

    #: L2
    money_after_milkshake = total_earnings - milkshake_cost # eval: 34.0 = 28 - -6.0

    #: L3
    money_in_wallet = money_after_milkshake / savings_fraction # eval: 17.0 = 34.0 / 2

    #: L4
    money_lost = money_in_wallet - money_left_unshredded # eval: 16.0 = 17.0 - 1

    #: FA
    answer = money_lost
    return answer # eval: return 16.0

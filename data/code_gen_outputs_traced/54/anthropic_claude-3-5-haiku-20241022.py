def solve(
    total_earnings: int = 28,  # Leah earned $28 working odd jobs
    milkshake_fraction: int = 7,  # she spent a seventh of it on a milkshake
    savings_fraction: int = 2,  # she put half of the rest in her savings account
    money_left_unshredded: int = 1  # her dog left $1 unshredded
):
    """Index: 54.
    Returns: the number of dollars Leah lost when her dog shredded her wallet."""
    #: L1
    milkshake_cost = total_earnings / milkshake_fraction # eval: 4.0 = 28 / 7
    #: L2
    money_after_milkshake = total_earnings - milkshake_cost # eval: 24.0 = 28 - 4.0
    #: L3
    money_in_wallet = money_after_milkshake / savings_fraction # eval: 12.0 = 24.0 / 2
    #: L4
    money_lost = money_in_wallet - money_left_unshredded # eval: 11.0 = 12.0 - 1
    answer = money_lost  # FINAL ANSWER # eval: 11.0 = 11.0  # FINAL ANSWER
    return answer # eval: return 11.0
def solve(
    initial_earnings: int = 28, # Leah earned $28 working odd jobs around the neighborhood.
    milkshake_cost_fraction: float = 1/7, # She spent a seventh of it on a milkshake
    savings_fraction: float = 1/2, # and put half of the rest in her savings account.
    money_left_after_shredding: int = 1 # Her dog got ahold of her wallet and shredded all the money inside but $1.
):
    """Index: 54.
    Returns: the amount of money Leah lost.
    """

    #: L1
    milkshake_cost = initial_earnings * milkshake_cost_fraction # eval: 4.0 = 28 * 0.14285714285714285

    #: L2

    #: L3
    money_in_wallet = money_left_after_shredding * savings_fraction # eval: 0.5 = 1 * 0.5

    #: L4
    money_lost = money_in_wallet - money_left_after_shredding # eval: -0.5 = 0.5 - 1

    #: FA
    answer = money_lost
    return answer # eval: return -0.5

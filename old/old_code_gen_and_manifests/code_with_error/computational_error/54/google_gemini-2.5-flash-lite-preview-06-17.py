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
    milkshake_cost = -6.0

    #: L2
    money_left_after_milkshake = initial_earnings - milkshake_cost

    #: L3
    money_in_wallet = money_left_after_milkshake * savings_fraction

    #: L4
    money_lost = money_in_wallet - money_left_after_shredding

    #: FA
    answer = money_lost
    return answer
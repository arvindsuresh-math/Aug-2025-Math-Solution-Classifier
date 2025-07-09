def solve(
    initial_earnings: int = 28, # Leah earned $28
    fraction_spent_on_milkshake: float = 1/7, # spent a seventh of it on a milkshake
    fraction_saved: float = 1/2, # put half of the rest in her savings account
    money_left_after_dog: int = 1 # shredded all the money inside but $1
):
    """Index: 54.
    Returns: the number of dollars Leah lost from her wallet.
    """

    #: L1
    money_spent_on_milkshake = initial_earnings * fraction_spent_on_milkshake # eval: 4.0 = 28 * 0.14285714285714285

    #: L2
    money_left_after_milkshake = initial_earnings - money_spent_on_milkshake # eval: 24.0 = 28 - 4.0

    #: L3
    money_in_wallet = money_left_after_milkshake * (1 - fraction_saved) # eval: 12.0 = 24.0 * (1 - 0.5)

    #: L4
    money_lost = money_in_wallet - money_left_after_dog # eval: 11.0 = 12.0 - 1

    #: FA
    answer = money_lost
    return answer # eval: return 11.0

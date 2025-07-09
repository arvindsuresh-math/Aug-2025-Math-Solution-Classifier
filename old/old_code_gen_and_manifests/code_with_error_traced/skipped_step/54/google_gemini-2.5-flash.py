def solve(
        earned_money: int = 28, # Leah earned $28
        milkshake_fraction_denominator: int = 7, # spent a seventh of it on a milkshake
        savings_fraction_denominator: int = 2, # put half of the rest in her savings account
        money_left_after_dog: int = 1 # shredded all the money inside but $1
    ):
    """Index: 54.
    Returns: the number of dollars Leah lost.
    """

    #: L1
    money_spent_on_milkshake = earned_money / milkshake_fraction_denominator # eval: 4.0 = 28 / 7

    #: L2

    #: L3
    money_in_wallet = earned_money / savings_fraction_denominator # eval: 14.0 = 28 / 2

    #: L4
    money_lost = money_in_wallet - money_left_after_dog # eval: 13.0 = 14.0 - 1

    #: FA
    answer = money_lost
    return answer # eval: return 13.0

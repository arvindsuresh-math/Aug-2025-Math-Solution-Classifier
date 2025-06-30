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
    money_spent_on_milkshake = money_left_after_dog / milkshake_fraction_denominator

    #: L2
    money_left_after_milkshake = earned_money - money_spent_on_milkshake

    #: L3
    money_in_wallet = money_left_after_milkshake / savings_fraction_denominator

    #: L4
    money_lost = money_in_wallet - money_left_after_dog

    #: FA
    answer = money_lost
    return answer
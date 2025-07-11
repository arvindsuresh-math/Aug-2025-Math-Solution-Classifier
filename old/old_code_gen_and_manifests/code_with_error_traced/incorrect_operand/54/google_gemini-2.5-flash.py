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
    money_spent_on_milkshake = money_left_after_dog / milkshake_fraction_denominator # eval: 0.14285714285714285 = 1 / 7

    #: L2
    money_left_after_milkshake = earned_money - money_spent_on_milkshake # eval: 27.857142857142858 = 28 - 0.14285714285714285

    #: L3
    money_in_wallet = money_left_after_milkshake / savings_fraction_denominator # eval: 13.928571428571429 = 27.857142857142858 / 2

    #: L4
    money_lost = money_in_wallet - money_left_after_dog # eval: 12.928571428571429 = 13.928571428571429 - 1

    #: FA
    answer = money_lost
    return answer # eval: return 12.928571428571429

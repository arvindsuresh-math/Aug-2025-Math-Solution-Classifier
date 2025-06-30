def solve(
    price_per_craft: int = 12, # Hillary sells handmade crafts for 12 dollars per craft
    crafts_sold: int = 3, # Hillary sells 3 crafts
    extra_money: int = 7, # is given an extra 7 dollars from an appreciative customer
    money_deposited: int = 18 # Hillary deposits 18 dollars from today's profits into her bank account
):
    """Index: 71.
    Returns: the amount of dollars Hillary is left with after making the deposit.
    """
    #: L1
    total_from_crafts = crafts_sold * price_per_craft

    #: L2
    total_before_deposit = total_from_crafts + extra_money

    #: L3
    money_left = total_before_deposit - money_deposited

    answer = money_left # FINAL ANSWER
    return answer
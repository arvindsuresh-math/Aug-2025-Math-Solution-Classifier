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
    total_from_crafts = crafts_sold * price_per_craft # eval: 36 = 3 * 12

    #: L2
    total_before_deposit = total_from_crafts + extra_money # eval: 43 = 36 + 7

    #: L3
    money_left = money_deposited - money_deposited # eval: 0 = 18 - 18

    #: FA
    answer = money_left
    return answer # eval: return 0

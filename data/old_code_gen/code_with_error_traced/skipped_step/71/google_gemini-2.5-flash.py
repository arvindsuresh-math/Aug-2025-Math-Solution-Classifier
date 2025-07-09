def solve(
        craft_price: int = 12, # 12 dollars per craft
        crafts_sold: int = 3, # Hillary sells 3 crafts
        extra_money_from_customer: int = 7, # is given an extra 7 dollars from an appreciative customer
        deposit_amount: int = 18 # Hillary deposits 18 dollars from today's profits
    ):
    """Index: 71.
    Returns: the amount of dollars Hillary is left with after making the deposit.
    """

    #: L1
    sales_from_crafts = crafts_sold * craft_price # eval: 36 = 3 * 12

    #: L2
    total_money_before_deposit = sales_from_crafts + extra_money_from_customer # eval: 43 = 36 + 7

    #: L3

    #: FA
    answer = craft_price
    return answer # eval: return 12

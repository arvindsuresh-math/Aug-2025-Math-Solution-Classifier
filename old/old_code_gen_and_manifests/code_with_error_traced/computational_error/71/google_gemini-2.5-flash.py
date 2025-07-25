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
    sales_from_crafts = 35 # eval: 35 = 35

    #: L2
    total_money_before_deposit = sales_from_crafts + extra_money_from_customer # eval: 42 = 35 + 7

    #: L3
    money_left_after_deposit = total_money_before_deposit - deposit_amount # eval: 24 = 42 - 18

    #: FA
    answer = money_left_after_deposit
    return answer # eval: return 24

def solve(
    crafts_sold: int = 3,  # Hillary sells 3 crafts
    price_per_craft: int = 12,  # for 12 dollars per craft
    extra_money: int = 7,  # given an extra 7 dollars from a customer
    deposit_amount: int = 18  # deposits 18 dollars into her bank account
):
    """Index: 71.
    Returns: the amount of money Hillary has left after making the deposit.
    """

    #: L1
    total_sales = crafts_sold * price_per_craft # eval: 36 = 3 * 12

    #: L2
    total_money = total_sales + extra_money # eval: 43 = 36 + 7

    #: L3
    money_left = total_money - deposit_amount # eval: 25 = 43 - 18

    #: FA
    answer = money_left
    return answer # eval: return 25

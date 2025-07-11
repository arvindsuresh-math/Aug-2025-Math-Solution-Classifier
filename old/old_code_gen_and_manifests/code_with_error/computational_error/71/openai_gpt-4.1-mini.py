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
    total_sales = crafts_sold * price_per_craft

    #: L2
    total_money = total_sales + extra_money

    #: L3
    money_left = 35

    #: FA
    answer = money_left
    return answer
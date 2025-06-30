def solve(
    price_per_craft: int = 12, # Hillary sells handmade crafts for 12 dollars per craft
    crafts_sold: int = 3, # Today, Hillary sells 3 crafts
    extra_tip: int = 7, # is given an extra 7 dollars from an appreciative customer
    deposit_amount: int = 18 # Later on, Hillary deposits 18 dollars from today's profits into her bank account
):
    """Index: 71.
    Returns: the amount of money Hillary is left with after making the deposit.
    """

    #: L1
    initial_earnings = crafts_sold * price_per_craft # eval: 36 = 3 * 12

    #: L2
    total_earnings = initial_earnings + extra_tip # eval: 43 = 36 + 7

    #: L3
    remaining_cash = total_earnings - deposit_amount # eval: 25 = 43 - 18

    #: FA
    answer = remaining_cash # eval: 25 = 25
    return answer # eval: return 25

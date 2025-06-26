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
    initial_earnings = crafts_sold * price_per_craft

    #: L2
    total_earnings = initial_earnings + extra_tip

    #: L3
    remaining_cash = total_earnings - deposit_amount

    answer = remaining_cash # FINAL ANSWER
    return answer
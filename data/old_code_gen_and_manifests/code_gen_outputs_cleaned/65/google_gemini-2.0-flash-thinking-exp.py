def solve(
    charge_per_lawn: int = 33, # charges $33
    lawns_mowed: int = 16, # mowed 16 lawns
    customers_tipped: int = 3, # three customers
    tip_amount: int = 10 # gave him a $10 tip
):
    """Index: 65.
    Returns: the total amount Lee earned mowing lawns last week.
    """
    #: L1
    earnings_from_mowing = charge_per_lawn * lawns_mowed

    #: L2
    earnings_from_tips = customers_tipped * tip_amount

    #: L3
    total_earnings = earnings_from_mowing + earnings_from_tips

    #: L4
    # Lee earned $558 mowing lawns last week.

    answer = total_earnings # FINAL ANSWER
    return answer
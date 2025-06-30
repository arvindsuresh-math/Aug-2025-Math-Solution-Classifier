def solve(
    charge_per_lawn: int = 33, # Lee mows one lawn and charges $33
    lawns_mowed_last_week: int = 16, # Last week he mowed 16 lawns
    num_customers_tip: int = 3, # three customers
    tip_per_customer: int = 10 # each gave him a $10 tip
):
    """Index: 65.
    Returns: the total amount of dollars Lee earned mowing lawns last week.
    """

    #: L1
    earnings_from_mowing = charge_per_lawn * lawns_mowed_last_week

    #: L2
    total_tips = num_customers_tip * tip_per_customer

    #: L3
    total_earnings = earnings_from_mowing + total_tips

    #: FA
    answer = total_earnings
    return answer
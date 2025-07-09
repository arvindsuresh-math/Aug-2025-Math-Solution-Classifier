def solve(
    charge_per_lawn: int = 33,  # Lee charges $33 per lawn
    lawns_mowed_last_week: int = 16,  # Lee mowed 16 lawns last week
    num_customers_tipping: int = 3,  # three customers gave tips
    tip_amount_per_customer: int = 10  # each tip was $10
):
    """Index: 65.
    Returns: the total amount of money Lee earned mowing lawns last week.
    """

    #: L1
    earnings_from_lawns = charge_per_lawn * lawns_mowed_last_week

    #: L2
    total_tips = num_customers_tipping * tip_amount_per_customer

    #: L3
    total_earnings = earnings_from_lawns + total_tips

    #: FA
    answer = total_earnings
    return answer
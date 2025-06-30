def solve(
        lawn_charge: int = 33, # Lee mows one lawn and charges $33
        lawns_mowed_last_week: int = 16, # Last week he mowed 16 lawns
        num_customers_tipped: int = 3, # three customers each gave him a $10 tip
        tip_amount: int = 10 # a $10 tip
    ):
    """Index: 65.
    Returns: the total dollars Lee earned mowing lawns last week.
    """

    #: L1
    earnings_from_mowing = 538

    #: L2
    total_tips = num_customers_tipped * tip_amount

    #: L3
    total_earnings = earnings_from_mowing + total_tips

    #: FA
    answer = total_earnings
    return answer
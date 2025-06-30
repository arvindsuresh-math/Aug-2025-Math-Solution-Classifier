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
    earnings_from_mowing = lawn_charge * lawns_mowed_last_week # eval: 528 = 33 * 16
    #: L2
    total_tips = num_customers_tipped * tip_amount # eval: 30 = 3 * 10
    #: L3
    total_earnings = earnings_from_mowing + total_tips # eval: 558 = 528 + 30
    answer = total_earnings # FINAL ANSWER # eval: 558 = 558 # FINAL ANSWER
    return answer # eval: return 558
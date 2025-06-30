def solve(
    charge_per_lawn: int = 33,  # Lee charges $33 per lawn
    lawns_mowed: int = 16,      # Lee mowed 16 lawns last week
    num_tips: int = 3,          # three customers gave him tips
    tip_amount: int = 10        # each tip was $10
):
    """Index: 65.
    Returns: the total amount of money Lee earned mowing lawns last week.
    """
    #: L1
    earnings_from_lawns = charge_per_lawn * lawns_mowed

    #: L2
    total_tips = num_tips * tip_amount

    #: L3
    total_earnings = earnings_from_lawns + total_tips

    answer = total_earnings  # FINAL ANSWER
    return answer
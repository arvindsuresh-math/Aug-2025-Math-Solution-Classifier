def solve(
    base_lawn_charge: int = 33,  # Lee charges $33 per lawn
    lawns_mowed: int = 16,  # Last week he mowed 16 lawns
    num_tipping_customers: int = 3,  # three customers gave him a tip
    tip_amount: int = 10  # each tip was $10
):
    """Index: 65.
    Returns: the total amount Lee earned from mowing lawns last week."""
    #: L1
    total_base_earnings = base_lawn_charge * lawns_mowed

    #: L2
    total_tips = num_tipping_customers * tip_amount

    #: L3
    total_earnings = total_base_earnings + total_tips

    answer = total_earnings  # FINAL ANSWER
    return answer
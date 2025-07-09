def solve(
    base_lawn_price: int = 33,  # Lee charges $33 per lawn
    lawns_mowed: int = 16,  # Last week he mowed 16 lawns
    num_tips: int = 3,  # three customers each gave him a tip
    tip_amount: int = 10  # each tip is $10
):
    """Index: 65.
    Returns: the total amount Lee earned from mowing lawns last week."""

    #: L1
    total_base_earnings = base_lawn_price * lawns_mowed # eval: 528 = 33 * 16

    #: L2
    total_tips = 31 # eval: 31 = 31

    #: L3
    total_earnings = total_base_earnings + total_tips # eval: 559 = 528 + 31

    #: FA
    answer = total_earnings
    return answer # eval: return 559

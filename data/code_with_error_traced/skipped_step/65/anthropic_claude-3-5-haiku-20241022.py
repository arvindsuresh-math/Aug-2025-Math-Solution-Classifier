def solve(
    base_lawn_price: int = 33,  # Lee charges $33 per lawn
    lawns_mowed: int = 16,  # Last week he mowed 16 lawns
    num_tips: int = 3,  # three customers each gave him a tip
    tip_amount: int = 10  # each tip is $10
):
    """Index: 65.
    Returns: the total amount Lee earned from mowing lawns last week."""

    #: L1

    #: L2
    total_tips = num_tips * tip_amount # eval: 30 = 3 * 10

    #: L3
    total_earnings = base_lawn_price + total_tips # eval: 63 = 33 + 30

    #: FA
    answer = total_earnings
    return answer # eval: return 63

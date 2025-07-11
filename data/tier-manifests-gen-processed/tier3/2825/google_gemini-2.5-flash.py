def solve():
    """Index: 2825.
    Returns: the worth of the entire lot.
    """
    # L1
    amount_sold_for = 460 # for the amount of $460
    share_fraction_denominator = 10 # 1/10 of his share
    mans_share_worth = amount_sold_for * share_fraction_denominator

    # L2
    whole_lot_fraction_denominator = 2 # 1/2 of a lot
    entire_lot_worth = mans_share_worth * whole_lot_fraction_denominator

    # FA
    answer = entire_lot_worth
    return answer
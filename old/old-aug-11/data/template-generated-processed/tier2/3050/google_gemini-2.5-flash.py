def solve():
    """Index: 3050.
    Returns: the number of muffins Janet bought.
    """
    # L1
    paid_amount = 20 # Janet paid $20
    change_back = 11 # got $11 in change back
    muffins_total_cost = paid_amount - change_back

    # L2
    muffin_cost_cents = 75 # Each muffin is 75 cents
    muffin_cost_dollars = 0.75 # used as .75 in calculation
    num_muffins = muffins_total_cost / muffin_cost_dollars

    # FA
    answer = num_muffins
    return answer
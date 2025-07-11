def solve():
    """Index: 1528.
    Returns: the amount of money Gabby still needs to buy the set.
    """
    # L1
    makeup_set_cost = 65 # The makeup set costs $65
    already_saved = 35 # she already has $35
    remaining_after_initial_save = makeup_set_cost - already_saved

    # L2
    mom_gift = 20 # Gabby’s mom gives her an additional $20
    needed_after_mom_gift = remaining_after_initial_save - mom_gift

    # FA
    answer = needed_after_mom_gift
    return answer
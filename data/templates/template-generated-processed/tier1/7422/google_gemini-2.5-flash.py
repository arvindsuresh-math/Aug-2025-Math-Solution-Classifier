def solve():
    """Index: 7422.
    Returns: the amount of punch Mark initially added to the bowl.
    """
    # L1
    bowl_capacity = 16 # 16 gallons of punch
    gallons_added_to_fill = 12 # add 12 gallons of punch to completely fill the bowl
    punch_before_final_add = bowl_capacity - gallons_added_to_fill

    # L2
    sally_drank = 2 # drinks 2 more gallons of punch
    punch_before_sally = punch_before_final_add + sally_drank

    # L3
    mark_added_refill = 4 # adds 4 more gallons
    punch_before_mark_refill = punch_before_sally - mark_added_refill

    # L4
    cousin_drank_multiplier = 2 # drinks half the punch
    initial_punch_added = punch_before_mark_refill * cousin_drank_multiplier

    # FA
    answer = initial_punch_added
    return answer
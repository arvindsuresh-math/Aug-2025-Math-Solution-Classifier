def solve():
    """Index: 2839.
    Returns: the number of additional marshmallows Jacob needs to buy.
    """
    # L1
    total_graham_crackers = 48 # 48 graham crackers
    graham_crackers_per_smore = 2 # two graham crackers
    marshmallows_needed_for_crackers = total_graham_crackers / graham_crackers_per_smore

    # L2
    marshmallows_on_hand = 6 # 6 marshmallows
    marshmallows_to_buy = marshmallows_needed_for_crackers - marshmallows_on_hand

    # FA
    answer = marshmallows_to_buy
    return answer
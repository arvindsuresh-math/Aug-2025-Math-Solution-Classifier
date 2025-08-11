def solve():
    """Index: 3143.
    Returns: the number of baskets Amy will fill.
    """
    # L1
    chocolate_bars = 5 # 5 chocolate bars
    mms_multiplier = 7 # 7 times as many M&Ms as chocolate bars
    mms = chocolate_bars * mms_multiplier

    # L2
    marshmallows_multiplier = 6 # 6 times as many marshmallows as M&Ms
    marshmallows = mms * marshmallows_multiplier

    # L3
    total_candies = chocolate_bars + mms + marshmallows

    # L4
    candies_per_basket = 10 # fills each basket with 10 candies
    num_baskets = total_candies / candies_per_basket

    # FA
    answer = num_baskets
    return answer
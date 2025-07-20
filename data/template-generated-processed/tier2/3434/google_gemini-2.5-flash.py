def solve():
    """Index: 3434.
    Returns: the amount of flour Lucy needs to buy.
    """
    # L1
    initial_flour_grams = 500 # a 500g bag of flour
    used_flour_grams = 240 # used 240g
    flour_after_baking = initial_flour_grams - used_flour_grams

    # L2
    spill_fraction = 0.5 # WK
    flour_after_spill = flour_after_baking * spill_fraction

    # L3
    flour_to_buy = initial_flour_grams - flour_after_spill

    # FA
    answer = flour_to_buy
    return answer
def solve(
        potatoes_produced: int = 237, # A garden produced 237 potatoes
        fewer_cucumbers: int = 60, # 60 fewer cucumbers
        peppers_multiplier: int = 2 # twice as many peppers
    ):
    """Index: 76.
    Returns: the total number of vegetables the garden produced.
    """

    #: L1

    #: L2
    peppers_produced = fewer_cucumbers * peppers_multiplier # eval: 120 = 60 * 2

    #: L3
    total_vegetables = potatoes_produced + fewer_cucumbers + peppers_produced # eval: 417 = 237 + 60 + 120

    #: FA
    answer = total_vegetables
    return answer # eval: return 417

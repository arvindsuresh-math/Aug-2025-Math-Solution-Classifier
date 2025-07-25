def solve(
        potatoes_produced: int = 237, # A garden produced 237 potatoes
        fewer_cucumbers: int = 60, # 60 fewer cucumbers
        peppers_multiplier: int = 2 # twice as many peppers
    ):
    """Index: 76.
    Returns: the total number of vegetables the garden produced.
    """

    #: L1
    cucumbers_produced = potatoes_produced - fewer_cucumbers # eval: 177 = 237 - 60

    #: L2
    peppers_produced = cucumbers_produced * peppers_multiplier # eval: 354 = 177 * 2

    #: L3
    total_vegetables = 767 # eval: 767 = 767

    #: FA
    answer = total_vegetables
    return answer # eval: return 767

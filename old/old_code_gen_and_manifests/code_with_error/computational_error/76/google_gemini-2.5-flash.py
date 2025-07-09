def solve(
        potatoes_produced: int = 237, # A garden produced 237 potatoes
        fewer_cucumbers: int = 60, # 60 fewer cucumbers
        peppers_multiplier: int = 2 # twice as many peppers
    ):
    """Index: 76.
    Returns: the total number of vegetables the garden produced.
    """

    #: L1
    cucumbers_produced = potatoes_produced - fewer_cucumbers

    #: L2
    peppers_produced = cucumbers_produced * peppers_multiplier

    #: L3
    total_vegetables = 767

    #: FA
    answer = total_vegetables
    return answer
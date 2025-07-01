def solve(
        potatoes_produced: int = 237, # A garden produced 237 potatoes
        fewer_cucumbers: int = 60, # 60 fewer cucumbers
        peppers_multiplier: int = 2 # twice as many peppers
    ):
    """Index: 76.
    Returns: the total number of vegetables the garden produced.
    """

    #: L1
    cucumbers_produced = fewer_cucumbers - fewer_cucumbers # eval: 0 = 60 - 60

    #: L2
    peppers_produced = cucumbers_produced * peppers_multiplier # eval: 0 = 0 * 2

    #: L3
    total_vegetables = potatoes_produced + cucumbers_produced + peppers_produced # eval: 237 = 237 + 0 + 0

    #: FA
    answer = total_vegetables
    return answer # eval: return 237

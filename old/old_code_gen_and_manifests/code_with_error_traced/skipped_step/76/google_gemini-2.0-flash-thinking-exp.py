def solve(
        num_potatoes: int = 237, # A garden produced 237 potatoes
        fewer_cucumbers_than_potatoes: int = 60, # 60 fewer cucumbers
        pepper_multiplier: int = 2 # twice as many peppers than the cucumbers
    ):
    """Index: 76.
    Returns: the total number of vegetables produced by the garden.
    """

    #: L1

    #: L2
    num_peppers = num_potatoes * pepper_multiplier # eval: 474 = 237 * 2

    #: L3
    total_vegetables = num_potatoes + num_potatoes + num_peppers # eval: 948 = 237 + 237 + 474

    #: FA
    answer = total_vegetables
    return answer # eval: return 948

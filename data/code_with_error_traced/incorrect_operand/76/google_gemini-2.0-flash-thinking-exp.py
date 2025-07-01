def solve(
        num_potatoes: int = 237, # A garden produced 237 potatoes
        fewer_cucumbers_than_potatoes: int = 60, # 60 fewer cucumbers
        pepper_multiplier: int = 2 # twice as many peppers than the cucumbers
    ):
    """Index: 76.
    Returns: the total number of vegetables produced by the garden.
    """

    #: L1
    num_cucumbers = pepper_multiplier - fewer_cucumbers_than_potatoes # eval: -58 = 2 - 60

    #: L2
    num_peppers = num_cucumbers * pepper_multiplier # eval: -116 = -58 * 2

    #: L3
    total_vegetables = num_potatoes + num_cucumbers + num_peppers # eval: 63 = 237 + -58 + -116

    #: FA
    answer = total_vegetables
    return answer # eval: return 63

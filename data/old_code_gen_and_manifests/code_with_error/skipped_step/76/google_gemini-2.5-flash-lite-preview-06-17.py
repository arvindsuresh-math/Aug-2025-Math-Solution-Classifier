def solve(
    num_potatoes: int = 237, # A garden produced 237 potatoes
    fewer_cucumbers: int = 60, # 60 fewer cucumbers
    peppers_multiplier: int = 2 # twice as many peppers than the cucumbers
):
    """Index: 76.
    Returns: the total number of vegetables the garden produced.
    """

    #: L1

    #: L2
    num_peppers = num_potatoes * peppers_multiplier

    #: L3
    total_vegetables = num_potatoes + num_potatoes + num_peppers

    #: FA
    answer = total_vegetables
    return answer
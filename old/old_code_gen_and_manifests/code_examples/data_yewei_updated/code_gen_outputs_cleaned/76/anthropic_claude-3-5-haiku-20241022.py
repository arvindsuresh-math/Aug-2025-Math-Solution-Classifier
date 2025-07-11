def solve(
    potatoes: int = 237,  # garden produced 237 potatoes
    cucumber_difference: int = 60  # 60 fewer cucumbers
    ):
    """Index: 76.
    Returns: the total number of vegetables produced by the garden.
    """
    #: L1
    cucumbers = potatoes - cucumber_difference

    #: L2
    peppers = cucumbers * 2

    #: L3
    total_vegetables = potatoes + cucumbers + peppers

    answer = total_vegetables  # FINAL ANSWER
    return answer
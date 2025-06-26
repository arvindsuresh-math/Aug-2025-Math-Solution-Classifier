def solve(
    potatoes: int = 237,  # A garden produced 237 potatoes
    fewer_cucumbers: int = 60  # 60 fewer cucumbers than potatoes
):
    """Index: 76.
    Returns: the total number of vegetables produced in the garden.
    """

    #: L1
    cucumbers = potatoes - fewer_cucumbers

    #: L2
    peppers = cucumbers * 2

    #: L3
    total_vegetables = potatoes + cucumbers + peppers

    answer = total_vegetables  # FINAL ANSWER
    return answer
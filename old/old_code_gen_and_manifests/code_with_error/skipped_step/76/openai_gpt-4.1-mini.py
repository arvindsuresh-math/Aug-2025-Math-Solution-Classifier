def solve(
    potatoes: int = 237,  # A garden produced 237 potatoes
    fewer_cucumbers: int = 60  # 60 fewer cucumbers than potatoes
):
    """Index: 76.
    Returns: the total number of vegetables produced in the garden.
    """

    #: L1

    #: L2
    peppers = fewer_cucumbers * 2

    #: L3
    total_vegetables = potatoes + fewer_cucumbers + peppers

    #: FA
    answer = total_vegetables
    return answer
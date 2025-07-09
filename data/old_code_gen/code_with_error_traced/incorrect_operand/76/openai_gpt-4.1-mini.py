def solve(
    potatoes: int = 237,  # A garden produced 237 potatoes
    fewer_cucumbers: int = 60  # 60 fewer cucumbers than potatoes
):
    """Index: 76.
    Returns: the total number of vegetables produced in the garden.
    """

    #: L1
    cucumbers = fewer_cucumbers - fewer_cucumbers # eval: 0 = 60 - 60

    #: L2
    peppers = cucumbers * 2 # eval: 0 = 0 * 2

    #: L3
    total_vegetables = potatoes + cucumbers + peppers # eval: 237 = 237 + 0 + 0

    #: FA
    answer = total_vegetables
    return answer # eval: return 237

def solve(
    potatoes: int = 237,  # A garden produced 237 potatoes
    fewer_cucumbers: int = 60  # 60 fewer cucumbers than potatoes
):
    """Index: 76.
    Returns: the total number of vegetables produced in the garden.
    """

    #: L1
    cucumbers = potatoes - fewer_cucumbers # eval: 177 = 237 - 60

    #: L2
    peppers = 364 # eval: 364 = 364

    #: L3
    total_vegetables = potatoes + cucumbers + peppers # eval: 778 = 237 + 177 + 364

    #: FA
    answer = total_vegetables
    return answer # eval: return 778

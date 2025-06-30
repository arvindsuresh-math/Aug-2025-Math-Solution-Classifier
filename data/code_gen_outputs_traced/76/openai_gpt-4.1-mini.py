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
    peppers = cucumbers * 2 # eval: 354 = 177 * 2
    #: L3
    total_vegetables = potatoes + cucumbers + peppers # eval: 768 = 237 + 177 + 354
    answer = total_vegetables  # FINAL ANSWER # eval: 768 = 768  # FINAL ANSWER
    return answer # eval: return 768
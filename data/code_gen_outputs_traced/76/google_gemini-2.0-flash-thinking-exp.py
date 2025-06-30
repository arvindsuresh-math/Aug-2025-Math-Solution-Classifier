def solve(
        num_potatoes: int = 237, # A garden produced 237 potatoes
        fewer_cucumbers_than_potatoes: int = 60, # 60 fewer cucumbers
        pepper_multiplier: int = 2 # twice as many peppers than the cucumbers
    ):
    """Index: 76.
    Returns: the total number of vegetables produced by the garden.
    """
    #: L1
    num_cucumbers = num_potatoes - fewer_cucumbers_than_potatoes # eval: 177 = 237 - 60
    #: L2
    num_peppers = num_cucumbers * pepper_multiplier # eval: 354 = 177 * 2
    #: L3
    total_vegetables = num_potatoes + num_cucumbers + num_peppers # eval: 768 = 237 + 177 + 354
    answer = total_vegetables # FINAL ANSWER # eval: 768 = 768 # FINAL ANSWER
    return answer # eval: return 768
def solve():
    """Index: 76.
    Returns: the total number of vegetables the garden produced.
    """
    # L1
    potatoes = 237 # 237 potatoes
    fewer_cucumbers = 60 # 60 fewer cucumbers
    cucumbers = potatoes - fewer_cucumbers

    # L2
    peppers_per_cucumber = 2 # twice as many peppers than the cucumbers
    peppers = cucumbers * peppers_per_cucumber

    # L3
    total_vegetables = potatoes + cucumbers + peppers

    # FA
    answer = total_vegetables
    return answer
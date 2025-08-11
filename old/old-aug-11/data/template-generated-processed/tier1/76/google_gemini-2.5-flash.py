def solve():
    """Index: 76.
    Returns: the total number of vegetables the garden produced.
    """
    # L1
    potatoes_produced = 237 # 237 potatoes
    fewer_cucumbers = 60 # 60 fewer cucumbers
    cucumbers_produced = potatoes_produced - fewer_cucumbers

    # L2
    multiplier_for_peppers = 2 # twice as many peppers
    peppers_produced = cucumbers_produced * multiplier_for_peppers

    # L3
    total_vegetables = potatoes_produced + cucumbers_produced + peppers_produced

    # FA
    answer = total_vegetables
    return answer
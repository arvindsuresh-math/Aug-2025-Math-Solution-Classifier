def solve():
    """Index: 4406.
    Returns: the total number of petals Collin has.
    """
    # L1
    ingrid_total_flowers = 33 # her 33 flowers
    fraction_denominator = 3 # a third of her 33 flowers
    flowers_from_ingrid = ingrid_total_flowers / fraction_denominator

    # L2
    collin_initial_flowers = 25 # Collin has 25 flowers
    collin_total_flowers = collin_initial_flowers + flowers_from_ingrid

    # L3
    petals_per_flower = 4 # each flower has 4 petals
    total_petals = collin_total_flowers * petals_per_flower

    # FA
    answer = total_petals
    return answer
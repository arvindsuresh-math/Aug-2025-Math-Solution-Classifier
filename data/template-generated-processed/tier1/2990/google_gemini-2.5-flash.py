def solve():
    """Index: 2990.
    Returns: the total number of jewels the dragon owned in the end.
    """
    # L1
    multiplier_twice = 2 # twice as many
    stolen_jewels_initial = 3 # three prize jewels
    stolen_crown_jewels = multiplier_twice * stolen_jewels_initial

    # L2
    fraction_denominator_third = 3 # a third of the number
    jewels_before_theft = stolen_crown_jewels * fraction_denominator_third

    # L3
    total_jewels_end = jewels_before_theft + stolen_crown_jewels

    # FA
    answer = total_jewels_end
    return answer
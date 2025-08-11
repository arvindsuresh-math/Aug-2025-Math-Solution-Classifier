def solve():
    """Index: 2758.
    Returns: the number of bags of Doritos in each pile.
    """
    # L1
    total_bags_of_chips = 80 # Mohammad has 80 bags of chips
    doritos_fraction_denominator = 4 # One quarter of the bags of chips are Doritos
    num_dorito_bags = total_bags_of_chips / doritos_fraction_denominator

    # L2
    num_piles = 4 # split the bags of Doritos into 4 equal piles
    doritos_per_pile = num_dorito_bags / num_piles

    # FA
    answer = doritos_per_pile
    return answer
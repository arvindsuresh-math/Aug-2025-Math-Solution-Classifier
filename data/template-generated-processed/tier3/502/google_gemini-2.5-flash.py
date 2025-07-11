def solve():
    """Index: 502.
    Returns: the cost of a single stuffed animal in dollars.
    """
    # L1
    magnet_cost = 3 # If the Magnet cost $3
    divisor_for_sticker_calc = 1 # WK
    sticker_cost = magnet_cost / divisor_for_sticker_calc

    # L2
    stuffed_animals_fraction_denominator = 4 # one quarter the price
    cost_of_two_stuffed_animals = magnet_cost * stuffed_animals_fraction_denominator

    # L3
    number_of_stuffed_animals = 2 # two stuffed animals
    cost_of_single_stuffed_animal = cost_of_two_stuffed_animals / number_of_stuffed_animals

    # FA
    answer = cost_of_single_stuffed_animal
    return answer
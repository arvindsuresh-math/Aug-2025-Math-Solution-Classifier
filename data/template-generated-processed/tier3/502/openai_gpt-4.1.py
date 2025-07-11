def solve():
    """Index: 502.
    Returns: the cost in dollars of a single stuffed animal.
    """
    # L1
    magnet_cost = 3 # Magnet cost $3
    sticker_ratio = 3 # Magnet cost three times more than the sticker
    sticker_cost = magnet_cost / sticker_ratio

    # L2
    stuffed_animals_ratio = 1/4 # Magnet cost one quarter the price of the two stuffed animals combined
    two_stuffed_animals_cost = magnet_cost / stuffed_animals_ratio

    # L3
    stuffed_animals_count = 2 # two stuffed animals
    single_stuffed_animal_cost = two_stuffed_animals_cost / stuffed_animals_count

    # FA
    answer = single_stuffed_animal_cost
    return answer
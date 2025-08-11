def solve():
    """Index: 7071.
    Returns: the number of cards Keith started with.
    """
    # L1
    cards_left = 46 # There are now only 46 cards left
    multiplier_for_half = 2 # WK
    cards_before_dog_ate = multiplier_for_half * cards_left

    # L2
    new_cards_added = 8 # bought 8 new baseball trading cards
    initial_cards = cards_before_dog_ate - new_cards_added

    # FA
    answer = initial_cards
    return answer
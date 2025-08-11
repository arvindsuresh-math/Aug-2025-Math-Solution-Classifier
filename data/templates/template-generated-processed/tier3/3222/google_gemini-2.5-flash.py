def solve():
    """Index: 3222.
    Returns: the number of cards Rex has left.
    """
    # L1
    nicole_cards = 400 # Nicole collected 400 Pokemon cards
    cindy_multiplier = 2 # twice as many
    cindy_cards = nicole_cards * cindy_multiplier

    # L2
    nicole_cindy_combined_cards = nicole_cards + cindy_cards

    # L3
    rex_divisor = 2 # half of Nicole and Cindy's combined total
    rex_initial_cards = nicole_cindy_combined_cards / rex_divisor

    # L4
    num_siblings = 3 # three younger siblings
    rex_share = 1 # WK
    total_recipients = num_siblings + rex_share
    rex_remaining_cards = rex_initial_cards / total_recipients

    # FA
    answer = rex_remaining_cards
    return answer
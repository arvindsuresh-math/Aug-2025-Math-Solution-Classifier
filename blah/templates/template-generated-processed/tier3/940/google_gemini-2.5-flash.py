def solve():
    """Index: 940.
    Returns: the number of additional cards they should collect.
    """
    # L1
    michael_cards = 100 # Michael has 100 cards now
    fewer_than_michael = 10 # 10 fewer cards than Michael
    mark_cards = michael_cards - fewer_than_michael

    # L2
    lloyd_multiplier = 3 # thrice as many cards as Lloyd
    lloyd_cards = mark_cards / lloyd_multiplier

    # L3
    current_total_cards = mark_cards + lloyd_cards + michael_cards

    # L4
    target_total_cards = 300 # total of 300 cards
    cards_to_collect = target_total_cards - current_total_cards

    # FA
    answer = cards_to_collect
    return answer
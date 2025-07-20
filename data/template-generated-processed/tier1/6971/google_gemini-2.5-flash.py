def solve():
    """Index: 6971.
    Returns: the total number of cards in the bag.
    """
    # L1
    hockey_cards = 200 # 200 hockey cards
    football_multiplier = 4 # 4 times as many football cards
    football_cards = football_multiplier * hockey_cards

    # L2
    football_hockey_total = football_cards + hockey_cards

    # L3
    baseball_fewer_than_football = 50 # 50 fewer baseball cards than football cards
    baseball_cards = football_cards - baseball_fewer_than_football

    # L4
    total_cards = baseball_cards + football_hockey_total

    # FA
    answer = total_cards
    return answer
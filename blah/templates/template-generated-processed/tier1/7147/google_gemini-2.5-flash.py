def solve():
    """Index: 7147.
    Returns: the number of weeks until Jed has 40 cards.
    """
    # L1
    started_cards = 20 # started with 20 cards
    cards_per_week_gain = 6 # gets 6 cards
    cards_end_week1 = started_cards + cards_per_week_gain

    # L2
    cards_before_giveaway_week2 = cards_end_week1 + cards_per_week_gain

    # L3
    cards_given_away_biweekly = 2 # gives 2 cards to his friends
    cards_end_week2 = cards_before_giveaway_week2 - cards_given_away_biweekly

    # L4
    cards_end_week3 = cards_end_week2 + cards_per_week_gain

    # L5
    cards_before_giveaway_week4 = cards_end_week3 + cards_per_week_gain

    # L6
    cards_end_week4 = cards_before_giveaway_week4 - cards_given_away_biweekly

    # FA
    answer = 4
    return answer
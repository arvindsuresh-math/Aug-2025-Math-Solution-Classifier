def solve():
    """Index: 3860.
    Returns: the total cost of the cows.
    """
    # Values derived from the question, used in subsequent steps
    hearts_per_card = 4 # 4 hearts on a card
    num_cards_in_deck = 52 # standard deck of 52 playing cards
    total_hearts_in_deck = hearts_per_card * num_cards_in_deck

    # L2
    multiplier_cows = 2 # twice as many cows
    num_cows = multiplier_cows * total_hearts_in_deck

    # L3
    price_per_cow = 200 # $200 each
    total_cost = num_cows * price_per_cow

    # FA
    answer = total_cost
    return answer
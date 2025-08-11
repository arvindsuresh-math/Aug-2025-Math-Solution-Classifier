def solve():
    """Index: 631.
    Returns: the cost of one deck of basketball cards.
    """
    # L1
    number_of_sunglasses_pairs = 2 # two pairs of sunglasses
    cost_per_sunglasses_pair = 50 # $50 each
    cost_of_sunglasses = number_of_sunglasses_pairs * cost_per_sunglasses_pair

    # L2
    cost_of_jeans = 100 # a pair of jeans for $100
    mary_total_spent = cost_of_sunglasses + cost_of_jeans

    # L3
    cost_of_shoes = 150 # a pair of shoes at $150
    cost_of_two_decks = mary_total_spent - cost_of_shoes

    # L4
    number_of_decks = 2 # two decks of basketball cards
    cost_of_one_deck = cost_of_two_decks / number_of_decks

    # FA
    answer = cost_of_one_deck
    return answer
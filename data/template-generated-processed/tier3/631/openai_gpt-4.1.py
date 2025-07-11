def solve():
    """Index: 631.
    Returns: the cost of one deck of basketball cards.
    """
    # L1
    sunglasses_pairs = 2 # two pairs of sunglasses
    sunglasses_price = 50 # $50 each
    sunglasses_total = sunglasses_pairs * sunglasses_price

    # L2
    jeans_price = 100 # a pair of jeans for $100
    mary_total = sunglasses_total + jeans_price

    # L3
    rose_shoes_price = 150 # a pair of shoes at $150
    two_decks_price = mary_total - rose_shoes_price

    # L4
    decks_count = 2 # two decks of basketball cards
    one_deck_price = two_decks_price / decks_count

    # FA
    answer = one_deck_price
    return answer
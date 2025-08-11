def solve():
    """Index: 2068.
    Returns: the number of cards Janessa kept for herself.
    """
    # L1
    janessa_own_cards = 4 # Janessa has 4 cards
    father_cards = 13 # 13 that her father gave her
    initial_cards = janessa_own_cards + father_cards

    # L2
    ebay_cards = 36 # ordered a collection of 36 cards from eBay
    total_cards = initial_cards + ebay_cards

    # L3
    bad_shape_cards = 4 # 4 cards are in bad shape
    good_cards = total_cards - bad_shape_cards

    # L4
    dexter_given = 29 # Janessa ended up giving Dexter 29 cards
    kept_cards = good_cards - dexter_given

    # FA
    answer = kept_cards
    return answer
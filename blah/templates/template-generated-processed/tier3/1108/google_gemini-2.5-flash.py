def solve():
    """Index: 1108.
    Returns: the number of more cards Ann has than Anton.
    """
    # L1
    ann_cards = 60 # Ann has 60 cards
    ann_heike_multiplier = 6 # six times as many cards as Heike
    heike_cards = ann_cards / ann_heike_multiplier

    # L2
    anton_heike_multiplier = 3 # three times as many cards in his collection as Heike does
    anton_cards = heike_cards * anton_heike_multiplier

    # L3
    difference_ann_anton = ann_cards - anton_cards

    # FA
    answer = difference_ann_anton
    return answer
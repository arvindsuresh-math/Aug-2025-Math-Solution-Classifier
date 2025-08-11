def solve():
    """Index: 4618.
    Returns: the total number of cards Dexter has.
    """
    # L1
    num_basketball_boxes = 9 # 9 boxes with basketball cards
    cards_per_basketball_box = 15 # each box has 15 cards
    total_basketball_cards = num_basketball_boxes * cards_per_basketball_box

    # L2
    fewer_football_boxes = 3 # 3 fewer plastic boxes with football cards
    num_football_boxes = num_basketball_boxes - fewer_football_boxes

    # L3
    cards_per_football_box = 20 # each box with 20 cards
    total_football_cards = num_football_boxes * cards_per_football_box

    # L4
    total_cards = total_basketball_cards + total_football_cards

    # FA
    answer = total_cards
    return answer
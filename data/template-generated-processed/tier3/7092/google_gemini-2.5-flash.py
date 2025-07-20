def solve():
    """Index: 7092.
    Returns: the weight of Brandon's textbooks.
    """
    # L1
    jon_book1_weight = 2 # two
    jon_book2_weight = 8 # eight
    jon_book3_weight = 5 # five
    jon_book4_weight = 9 # nine
    total_jon_textbook_weight = jon_book1_weight + jon_book2_weight + jon_book3_weight + jon_book4_weight

    # L2
    weight_multiplier = 3 # three times as much
    total_brandon_textbook_weight = total_jon_textbook_weight / weight_multiplier

    # FA
    answer = total_brandon_textbook_weight
    return answer
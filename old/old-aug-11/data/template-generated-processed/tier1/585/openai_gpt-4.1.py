def solve():
    """Index: 585.
    Returns: the number of additional cards needed for the pizza party.
    """
    # L1
    num_kids = 30 # 30 kids in the class
    cards_per_kid = 8 # everyone makes 8
    cards_made = num_kids * cards_per_kid

    # L2
    required_cards = 1000 # need to make 1000 Valentine's Day cards
    cards_needed = required_cards - cards_made

    # FA
    answer = cards_needed
    return answer
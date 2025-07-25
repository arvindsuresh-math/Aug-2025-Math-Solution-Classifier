def solve():
    """Index: 585.
    Returns: the number of additional cards needed to get a pizza party.
    """
    # L1
    num_kids = 30 # 30 kids in the class
    cards_per_kid = 8 # If everyone makes 8
    cards_made = num_kids * cards_per_kid

    # L2
    cards_needed_total = 1000 # make 1000 Valentine's Day cards
    cards_remaining_to_make = cards_needed_total - cards_made

    # FA
    answer = cards_remaining_to_make
    return answer
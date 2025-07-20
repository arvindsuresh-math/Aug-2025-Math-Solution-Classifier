def solve():
    """Index: 3353.
    Returns: the total number of cards Joseph had at first.
    """
    # L1
    cards_per_student = 23 # 23 cards to each
    num_students = 15 # 15 students
    cards_given_to_students = cards_per_student * num_students

    # L2
    cards_left = 12 # 12 cards left
    total_cards_at_first = cards_given_to_students + cards_left

    # FA
    answer = total_cards_at_first
    return answer
def solve():
    """Index: 963.
    Returns: the total number of children at the event.
    """
    # L1
    initial_men = 40 # 40 of them are men
    women_divisor = 2 # half the number of men are women
    women = initial_men / women_divisor

    # L2
    total_men_women = initial_men + women

    # L3
    total_guests = 80 # 80 guests
    initial_children = total_guests - total_men_women

    # L4
    added_children = 10 # added 10 children
    final_children = initial_children + added_children

    # FA
    answer = final_children
    return answer
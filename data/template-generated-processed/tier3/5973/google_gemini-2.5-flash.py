def solve():
    """Index: 5973.
    Returns: the number of best friends Nathaniel has.
    """
    # L1
    initial_tickets = 11 # Nathaniel has 11 tickets
    remaining_tickets = 3 # until he only has 3 tickets left
    tickets_given_away = initial_tickets - remaining_tickets

    # L2
    tickets_per_friend = 2 # gives away 2 tickets each to his best friends
    number_of_friends = tickets_given_away / tickets_per_friend

    # FA
    answer = number_of_friends
    return answer
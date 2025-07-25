def solve():
    """Index: 2580.
    Returns: the total number of friends.
    """
    # L1
    initial_oranges = 80 # Jillian had 80 oranges
    pieces_per_orange = 10 # divided each orange into ten equal pieces
    total_pieces = initial_oranges * pieces_per_orange

    # L2
    pieces_per_friend = 4 # each friend to get four pieces
    number_of_friends = total_pieces / pieces_per_friend

    # FA
    answer = number_of_friends
    return answer
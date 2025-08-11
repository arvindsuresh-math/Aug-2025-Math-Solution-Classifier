def solve():
    """Index: 4816.
    Returns: the number of friends Lyndee had over.
    """
    # L1
    total_chicken_pieces = 11 # Mrs. Crocker made 11 pieces of fried chicken
    lyndee_ate_pieces = 1 # Lyndee only ate one piece
    remaining_chicken_pieces = total_chicken_pieces - lyndee_ate_pieces

    # L2
    pieces_per_friend = 2 # each of her friends got to eat 2 pieces
    number_of_friends = remaining_chicken_pieces / pieces_per_friend

    # FA
    answer = number_of_friends
    return answer
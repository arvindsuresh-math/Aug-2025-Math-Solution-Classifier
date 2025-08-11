def solve():
    """Index: 4650.
    Returns: the total number of pieces of bread Sally eats.
    """
    # L1
    sandwiches_saturday = 2 # 2 sandwiches on Saturday
    sandwiches_sunday = 1 # 1 sandwich on Sunday
    total_sandwiches = sandwiches_saturday + sandwiches_sunday

    # L2
    pieces_per_sandwich = 2 # 2 pieces of bread
    total_pieces_of_bread = total_sandwiches * pieces_per_sandwich

    # FA
    answer = total_pieces_of_bread
    return answer
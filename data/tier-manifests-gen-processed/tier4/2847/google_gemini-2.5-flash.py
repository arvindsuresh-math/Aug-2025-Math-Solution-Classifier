def solve():
    """Index: 2847.
    Returns: the total number of mushrooms GiGi cut up at the beginning.
    """
    # L1
    kenny_pieces = 38 # 38 mushroom pieces on his pizza
    pieces_per_mushroom = 4 # cut each mushroom into 4 pieces
    kenny_mushrooms = kenny_pieces / pieces_per_mushroom

    # L2
    karla_pieces = 42 # 42 mushroom pieces on her pizza
    karla_mushrooms = karla_pieces / pieces_per_mushroom

    # L3
    total_mushrooms_used_by_twins = kenny_mushrooms + karla_mushrooms

    # L4
    remaining_pieces = 8 # 8 pieces of mushrooms remaining
    remaining_mushrooms = remaining_pieces / pieces_per_mushroom

    # L5
    total_mushrooms_cut = total_mushrooms_used_by_twins + remaining_mushrooms

    # FA
    answer = total_mushrooms_cut
    return answer
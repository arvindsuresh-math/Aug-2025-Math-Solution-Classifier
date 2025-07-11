def solve():
    """Index: 2847.
    Returns: the number of mushrooms GiGi cut up at the beginning.
    """
    # L1
    kenny_pieces = 38 # Kenny sprinkled 38 mushroom pieces on his pizza
    pieces_per_mushroom = 4 # She cut each mushroom into 4 pieces
    kenny_mushrooms = kenny_pieces / pieces_per_mushroom

    # L2
    karla_pieces = 42 # Karla sprinkled 42 mushroom pieces on her pizza
    karla_mushrooms = karla_pieces / pieces_per_mushroom

    # L3
    twins_mushrooms = kenny_mushrooms + karla_mushrooms

    # L4
    remaining_pieces = 8 # 8 pieces of mushrooms remaining
    remaining_mushrooms = remaining_pieces / pieces_per_mushroom

    # L5
    total_mushrooms = twins_mushrooms + remaining_mushrooms

    # FA
    answer = total_mushrooms
    return answer
def solve():
    """Index: 4412.
    Returns: the number of puzzle pieces still left to be placed.
    """
    # L1
    total_pieces = 300 # a 300 piece puzzle set
    num_sons = 3 # three sons
    pieces_per_son = total_pieces / num_sons

    # L2
    reyn_pieces = 25 # Reyn can place 25 pieces
    rhys_multiplier = 2 # twice as much as Reyn
    rhys_pieces = reyn_pieces * rhys_multiplier

    # L3
    rory_multiplier = 3 # three times as much as Reyn
    rory_pieces = reyn_pieces * rory_multiplier

    # L4
    total_pieces_placed = reyn_pieces + rhys_pieces + rory_pieces

    # L5
    pieces_left = total_pieces - total_pieces_placed

    # FA
    answer = pieces_left
    return answer
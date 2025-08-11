def solve():
    """Index: 4546.
    Returns: the number of chairs Gerald can make.
    """
    # L1
    pieces_per_table = 12 # 12 pieces of wood to make a table
    num_tables = 24 # if he makes 24 tables
    wood_for_tables = num_tables * pieces_per_table

    # L2
    total_wood_pieces = 672 # He has 672 pieces of wood
    remaining_wood = total_wood_pieces - wood_for_tables

    # L3
    pieces_per_chair = 8 # 8 pieces of wood to make a chair
    num_chairs = remaining_wood / pieces_per_chair

    # FA
    answer = num_chairs
    return answer
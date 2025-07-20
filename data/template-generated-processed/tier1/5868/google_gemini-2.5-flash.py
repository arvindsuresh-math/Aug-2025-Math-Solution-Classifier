def solve():
    """Index: 5868.
    Returns: the total amount spent on concrete blocks.
    """
    # L1
    pieces_per_section = 30 # 30 pieces of concrete blocks
    num_sections = 8 # eight sections
    total_blocks = pieces_per_section * num_sections

    # L2
    cost_per_piece = 2 # $2 per piece
    total_cost = total_blocks * cost_per_piece

    # FA
    answer = total_cost
    return answer
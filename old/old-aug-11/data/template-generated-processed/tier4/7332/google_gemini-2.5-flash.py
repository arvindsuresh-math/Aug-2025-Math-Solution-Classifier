def solve():
    """Index: 7332.
    Returns: the total cost of all art pieces.
    """
    # L1
    total_cost_first_3_pieces = 45000 # total price came to $45,000
    num_first_pieces = 3 # first 3 pieces of art
    cost_per_first_piece = total_cost_first_3_pieces / num_first_pieces

    # L2
    more_expensive_percent = 0.5 # 50% more expensive
    extra_cost_next_piece = cost_per_first_piece * more_expensive_percent

    # L3
    cost_next_piece = cost_per_first_piece + extra_cost_next_piece

    # L4
    total_art_cost = total_cost_first_3_pieces + cost_next_piece

    # FA
    answer = total_art_cost
    return answer
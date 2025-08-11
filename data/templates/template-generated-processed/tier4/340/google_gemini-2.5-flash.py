def solve():
    """Index: 340.
    Returns: the number of pieces of rope Tom needs to buy.
    """
    # L1
    feet_per_story = 10 # One story is 10 feet
    num_stories = 6 # 6 stories
    total_feet_needed = feet_per_story * num_stories

    # L2
    rope_length_initial = 20 # 20 feet long
    loss_percentage = 0.25 # lose 25% when lashing them together
    feet_lost_per_piece = rope_length_initial * loss_percentage

    # L3
    effective_rope_length_per_piece = rope_length_initial - feet_lost_per_piece

    # L4
    num_pieces_needed = total_feet_needed / effective_rope_length_per_piece

    # FA
    answer = num_pieces_needed
    return answer
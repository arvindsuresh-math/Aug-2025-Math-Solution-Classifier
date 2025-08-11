def solve():
    """Index: 340.
    Returns: the number of pieces of rope Tom needs to buy.
    """
    # L1
    feet_per_story = 10 # One story is 10 feet
    num_stories = 6 # 6 stories
    total_feet_needed = feet_per_story * num_stories

    # L2
    rope_length = 20 # The only rope being sold is 20 feet long
    lashing_loss_fraction = 0.25 # you lose 25% when lashing them together
    feet_lost_per_rope = rope_length * lashing_loss_fraction

    # L3
    usable_feet_per_rope = rope_length - feet_lost_per_rope

    # L4
    num_pieces = total_feet_needed / usable_feet_per_rope

    # FA
    answer = num_pieces
    return answer
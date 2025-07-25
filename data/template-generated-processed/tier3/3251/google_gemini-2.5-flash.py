def solve():
    """Index: 3251.
    Returns: the number of large balls Michael can make.
    """
    # L1
    small_balls_made = 22 # already made 22 small balls
    rubber_bands_per_small_ball = 50 # A small ball uses 50 rubber bands
    rubber_bands_used_for_small_balls = small_balls_made * rubber_bands_per_small_ball

    # L2
    total_pack_size = 5000 # brought a 5,000 pack
    remaining_rubber_bands = total_pack_size - rubber_bands_used_for_small_balls

    # L3
    rubber_bands_per_large_ball = 300 # A large ball requires 300 rubber bands
    num_large_balls = remaining_rubber_bands / rubber_bands_per_large_ball

    # FA
    answer = num_large_balls
    return answer
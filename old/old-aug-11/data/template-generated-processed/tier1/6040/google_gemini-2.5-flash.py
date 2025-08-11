def solve():
    """Index: 6040.
    Returns: the number of flyers left to be handed out.
    """
    # L1
    jack_flyers_handed = 120 # Jack handed 120 flyers
    rose_flyers_handed = 320 # Rose handed 320 flyers
    total_handed = jack_flyers_handed + rose_flyers_handed

    # L2
    total_flyers_initial = 1236 # They made 1,236 flyers
    flyers_left = total_flyers_initial - total_handed

    # FA
    answer = flyers_left
    return answer
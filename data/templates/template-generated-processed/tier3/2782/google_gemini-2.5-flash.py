def solve():
    """Index: 2782.
    Returns: the time it would take Moe to eat the target number of pieces of cuttlebone.
    """
    # L1
    time_to_eat_initial_pieces = 10 # 10 seconds to eat 40 pieces
    initial_pieces_eaten = 40 # 40 pieces of cuttlebone
    cuttlebones_per_second = initial_pieces_eaten / time_to_eat_initial_pieces

    # L2
    target_pieces = 800 # eat 800 pieces
    time_to_eat_target_pieces = target_pieces / cuttlebones_per_second

    # FA
    answer = time_to_eat_target_pieces
    return answer
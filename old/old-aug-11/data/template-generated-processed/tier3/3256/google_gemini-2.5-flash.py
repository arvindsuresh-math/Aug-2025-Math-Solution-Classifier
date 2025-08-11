def solve():
    """Index: 3256.
    Returns: the number of sandwiches Bert has left.
    """
    # L1
    initial_sandwiches = 12 # Bert made 12 sandwiches
    half_divisor = 2 # half of the sandwiches
    sandwiches_eaten_first_day = initial_sandwiches / half_divisor

    # L2
    less_sandwiches = 2 # 2 sandwiches less
    sandwiches_eaten_second_day = sandwiches_eaten_first_day - less_sandwiches

    # L3
    sandwiches_left = initial_sandwiches - sandwiches_eaten_first_day - sandwiches_eaten_second_day

    # FA
    answer = sandwiches_left
    return answer
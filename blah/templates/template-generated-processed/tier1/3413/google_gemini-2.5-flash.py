def solve():
    """Index: 3413.
    Returns: the total number of seeds Mike started with.
    """
    # L1
    seeds_left_group = 20 # 20 seeds to the birds on the left
    multiplier_right_group = 2 # twice as much
    seeds_right_group = seeds_left_group * multiplier_right_group

    # L2
    total_first_two_throws = seeds_left_group + seeds_right_group

    # L3
    seeds_more_birds = 30 # throws 30 more seeds
    seeds_left_over = 30 # has 30 seeds left
    initial_seeds = total_first_two_throws + seeds_more_birds + seeds_left_over

    # FA
    answer = initial_seeds
    return answer
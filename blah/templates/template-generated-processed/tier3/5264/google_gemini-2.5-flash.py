def solve():
    """Index: 5264.
    Returns: the number of cakes Julia has remaining.
    """
    # L1
    cakes_per_day_base = 5 # 5 cakes per day
    less_cakes = 1 # one less than 5 cakes
    cakes_per_day = cakes_per_day_base - less_cakes

    # L2
    num_days = 6 # for 6 days
    total_cakes_baked = cakes_per_day * num_days

    # L3
    eating_frequency_divisor = 2 # every other day
    cakes_eaten_by_clifford = num_days / eating_frequency_divisor

    # L4
    cakes_remaining = total_cakes_baked - cakes_eaten_by_clifford

    # FA
    answer = cakes_remaining
    return answer
def solve():
    """Index: 3846.
    Returns: the total number of popcorn kernels remaining on the ground.
    """
    # L1
    total_distance = 5000 # 5000 feet from her school
    drop_interval = 25 # 1 kernel of popcorn per 25 feet
    original_kernels_dropped = total_distance / drop_interval

    # L2
    squirrel_eats_denominator = 4 # one-quarter of the popcorn
    kernels_eaten_by_squirrel = original_kernels_dropped / squirrel_eats_denominator

    # L3
    remaining_kernels = original_kernels_dropped - kernels_eaten_by_squirrel

    # FA
    answer = remaining_kernels
    return answer
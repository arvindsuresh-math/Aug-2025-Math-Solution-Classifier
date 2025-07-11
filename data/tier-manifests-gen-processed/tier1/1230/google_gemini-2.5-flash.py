def solve():
    """Index: 1230.
    Returns: the total time in minutes to finish decorating fingernails and toenails.
    """
    # L1
    num_toenails = 10 # 10 toenails
    num_fingernails = 10 # 10 fingernails
    total_nails = num_toenails + num_fingernails

    # L2
    time_to_apply_coat = 20 # 20 minutes to apply each coat
    time_to_dry_coat = 20 # 20 minutes for each coat to dry
    time_per_coat_cycle = time_to_apply_coat + time_to_dry_coat

    # L3
    num_coats = 3 # a base coat, a coat of paint and a coat of glitter (3 different coats)
    total_time = time_per_coat_cycle * num_coats

    # FA
    answer = total_time
    return answer
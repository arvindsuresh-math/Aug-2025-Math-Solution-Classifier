def solve():
    """Index: 1230.
    Returns: the total number of minutes it will take Casey to finish decorating her fingernails and toenails.
    """
    # L1
    toenails = 10 # 10 toenails
    fingernails = 10 # 10 fingernails
    total_nails = toenails + fingernails

    # L2
    time_apply_coat = 20 # 20 minutes to apply each coat
    time_dry_coat = 20 # 20 minutes for each coat to dry
    time_per_coat = time_apply_coat + time_dry_coat

    # L3
    num_coats = 3 # base coat, paint, glitter
    total_time = time_per_coat * num_coats

    # FA
    answer = total_time
    return answer
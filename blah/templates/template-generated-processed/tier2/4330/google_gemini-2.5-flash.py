def solve():
    """Index: 4330.
    Returns: the total number of legos Simon has.
    """
    # L1
    bruce_more_than_kent = 20 # 20 more than Kent
    kent_legos = 40 # Kent has 40 legos
    bruce_legos = bruce_more_than_kent + kent_legos

    # L2
    simon_percent_more = 0.20 # 20% more legos
    simon_percent_more_num = 20 # 20% more legos
    percent_factor = 0.01 # WK
    simon_extra_legos = simon_percent_more_num * percent_factor * bruce_legos

    # L3
    simon_total_legos = simon_extra_legos + bruce_legos

    # FA
    answer = simon_total_legos
    return answer
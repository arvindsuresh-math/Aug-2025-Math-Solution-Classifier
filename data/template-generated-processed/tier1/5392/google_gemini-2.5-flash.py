def solve():
    """Index: 5392.
    Returns: the total number of spears Marcy can make.
    """
    # L1
    spears_per_sapling = 3 # 3 spears out of a sapling
    num_saplings = 6 # 6 saplings
    spears_from_saplings = spears_per_sapling * num_saplings

    # L2
    spears_from_log = 9 # 9 spears out of a log
    total_spears = spears_from_saplings + spears_from_log

    # FA
    answer = total_spears
    return answer
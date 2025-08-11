def solve():
    """Index: 2747.
    Returns: the total number of stamps Kylie and Nelly have together.
    """
    # L1
    kylie_stamps = 34 # Kylie has 34 stamps
    nelly_more_than_kylie = 44 # Nelly, has 44 more stamps than Kylie
    nelly_stamps = kylie_stamps + nelly_more_than_kylie

    # L2
    total_stamps = kylie_stamps + nelly_stamps

    # FA
    answer = total_stamps
    return answer
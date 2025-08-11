def solve():
    """Index: 377.
    Returns: the combined length of the CDs in hours.
    """
    # L1
    short_cd_length = 1.5 # Two of them are 1.5 hours each
    long_cd_multiplier = 2 # The last one is twice that long
    long_cd_length = short_cd_length * long_cd_multiplier

    # L2
    num_short_cds = 2 # Two of them
    combined_short_cds_length = short_cd_length * num_short_cds

    # L3
    total_length = long_cd_length + combined_short_cds_length

    # FA
    answer = total_length
    return answer
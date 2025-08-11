def solve():
    """Index: 377.
    Returns: the combined length of the CDs.
    """
    # L1
    short_cd_length = 1.5 # Two of them are 1.5 hours each
    long_cd_length = short_cd_length * 2

    # L2
    num_shorter_cds = 2 # Two of them are 1.5 hours each
    combined_short_cd_length = short_cd_length * num_shorter_cds

    # L3
    total_length = long_cd_length + combined_short_cd_length

    # FA
    answer = total_length
    return answer
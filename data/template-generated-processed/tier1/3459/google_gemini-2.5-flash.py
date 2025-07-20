def solve():
    """Index: 3459.
    Returns: the total number of CDs Kristine and Dawn have together.
    """
    # L1
    dawn_cds = 10 # Dawn has 10 CDs
    kristine_more_than_dawn = 7 # Kristine has 7 more CDs than Dawn
    kristine_cds = dawn_cds + kristine_more_than_dawn

    # L2
    total_cds = dawn_cds + kristine_cds

    # FA
    answer = total_cds
    return answer
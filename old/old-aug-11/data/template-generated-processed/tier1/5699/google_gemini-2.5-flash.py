def solve():
    """Index: 5699.
    Returns: the number of apples Yanna kept.
    """
    # L1
    total_apples = 60 # Yanna bought 60 apples
    zenny_apples = 18 # gave eighteen apples to Zenny
    apples_after_zenny = total_apples - zenny_apples

    # L2
    andrea_apples = 6 # gave six more apples to Andrea
    apples_after_andrea = apples_after_zenny - andrea_apples

    # FA
    answer = apples_after_andrea
    return answer
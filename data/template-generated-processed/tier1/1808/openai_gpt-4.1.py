def solve():
    """Index: 1808.
    Returns: how many more zits are in Mr. Jones' class than in Ms. Swanson's class.
    """
    # L1
    jones_avg_zits = 6 # average of six zits each
    jones_num_kids = 32 # 32 in Mr. Jones' class
    jones_total_zits = jones_avg_zits * jones_num_kids

    # L2
    swanson_avg_zits = 5 # average of 5 zits each
    swanson_num_kids = 25 # 25 kids in Ms. Swanson's class
    swanson_total_zits = swanson_avg_zits * swanson_num_kids

    # L3
    difference = jones_total_zits - swanson_total_zits

    # FA
    answer = difference
    return answer
def solve():
    """Index: 1808.
    Returns: the difference in the number of zits between Mr. Jones' class and Ms. Swanson's class.
    """
    # L1
    jones_avg_zits = 6 # average of six zits each
    jones_num_kids = 32 # 32 in Mr. Jones' class
    total_zits_jones_class = jones_avg_zits * jones_num_kids

    # L2
    swanson_avg_zits = 5 # average of 5 zits each
    swanson_num_kids = 25 # 25 kids in Ms. Swanson's class
    total_zits_swanson_class = swanson_avg_zits * swanson_num_kids

    # L3
    difference_in_zits = total_zits_jones_class - total_zits_swanson_class

    # FA
    answer = difference_in_zits
    return answer
def solve():
    """Index: 295.
    Returns: the number of bags of apples Pam has.
    """
    # L1
    gerald_bag_apples = 40 # Gerald's bags have 40 apples each
    pam_bag_multiplier = 3 # Each of her bags has as many apples as 3 of Gerald's bags
    pam_bag_apples = gerald_bag_apples * pam_bag_multiplier

    # L2
    pam_total_apples = 1200 # Pam has 1200 apples in total
    pam_bags = pam_total_apples / pam_bag_apples

    # FA
    answer = pam_bags
    return answer
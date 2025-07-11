def solve():
    """Index: 954.
    Returns: the total number of apples Pam has.
    """
    # L1
    gerald_bag_apples = 40 # Gerald's bags have 40 apples each
    pam_bag_multiple = 3 # Each of her bags has as many apples as 3 of Gerald's bags
    pam_bag_apples = gerald_bag_apples * pam_bag_multiple

    # L2
    pam_bags = 10 # Pam has 10 bags of apples
    pam_total_apples = pam_bag_apples * pam_bags

    # FA
    answer = pam_total_apples
    return answer
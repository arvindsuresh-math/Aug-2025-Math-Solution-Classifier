def solve():
    """Index: 295.
    Returns: the number of bags of apples Pam has.
    """
    # L1
    geralds_apples_per_bag = 40 # Gerald's bags have 40 apples each
    geralds_bags_equivalent = 3 # as many apples as 3 of Gerald's bags
    apples_per_pam_bag = geralds_apples_per_bag * geralds_bags_equivalent

    # L2
    total_pam_apples = 1200 # If Pam has 1200 apples in total
    pam_bags = total_pam_apples / apples_per_pam_bag

    # FA
    answer = pam_bags
    return answer
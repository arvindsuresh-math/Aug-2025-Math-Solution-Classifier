def solve():
    """Index: 954.
    Returns: the total number of apples Pam has.
    """
    # L1
    geralds_apples_per_bag = 40 # Gerald's bags have 40 apples each
    geralds_bags_equivalent_to_pams = 3 # as many apples as 3 of Gerald's bags
    apples_per_pams_bag = geralds_apples_per_bag * geralds_bags_equivalent_to_pams

    # L2
    pams_total_bags = 10 # 10 bags of apples
    total_apples_pam_has = apples_per_pams_bag * pams_total_bags

    # FA
    answer = total_apples_pam_has
    return answer
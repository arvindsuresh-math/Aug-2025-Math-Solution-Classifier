def solve():
    """Index: 2188.
    Returns: the total milligrams of zinc Jerry eats.
    """
    # L1
    big_antacid_weight_grams = 2 # 2 grams each
    num_big_antacids = 2 # 2 antacids
    total_big_weight_grams = big_antacid_weight_grams * num_big_antacids

    # L2
    mg_per_gram = 1000 # WK
    total_big_weight_mg = total_big_weight_grams * mg_per_gram

    # L3
    big_zinc_percent_num = 5 # 5% zinc
    percent_factor = 0.01 # WK
    big_zinc_mg = total_big_weight_mg * big_zinc_percent_num * percent_factor

    # L4
    num_small_antacids = 3 # three more smaller antacids
    small_antacid_weight_grams = 1 # 1 gram each
    total_small_weight_mg = num_small_antacids * small_antacid_weight_grams * mg_per_gram

    # L5
    small_zinc_percent_num = 15 # 15% zinc
    small_zinc_mg = total_small_weight_mg * small_zinc_percent_num * percent_factor

    # L6
    total_zinc_mg = small_zinc_mg + big_zinc_mg

    # FA
    answer = total_zinc_mg
    return answer
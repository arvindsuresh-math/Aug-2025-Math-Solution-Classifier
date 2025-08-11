def solve():
    """Index: 2188.
    Returns: the total milligrams of zinc Jerry eats.
    """
    # L1
    big_antacid_weight_per_pill = 2 # weigh 2 grams each
    num_big_antacids = 2 # 2 antacids
    total_weight_big_antacids_grams = big_antacid_weight_per_pill * num_big_antacids

    # L2
    mg_per_gram = 1000 # WK
    total_weight_big_antacids_mg = total_weight_big_antacids_grams * mg_per_gram

    # L3
    zinc_percent_big_antacids_num = 5 # 5% zinc by weight
    percent_to_decimal_factor = 0.01 # WK
    zinc_big_antacids_mg = total_weight_big_antacids_mg * zinc_percent_big_antacids_num * percent_to_decimal_factor

    # L4
    num_small_antacids = 3 # three more smaller antacids
    small_antacid_weight_per_pill = 1 # weigh 1 gram each
    total_weight_small_antacids_mg = num_small_antacids * small_antacid_weight_per_pill * mg_per_gram

    # L5
    zinc_percent_small_antacids_num = 15 # 15% zinc
    zinc_small_antacids_mg = total_weight_small_antacids_mg * (zinc_percent_small_antacids_num * percent_to_decimal_factor)

    # L6
    total_zinc_mg = zinc_small_antacids_mg + zinc_big_antacids_mg

    # FA
    answer = total_zinc_mg
    return answer
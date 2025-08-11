def solve():
    """Index: 6009.
    Returns: the total number of roses in Lorelei's vase.
    """
    # L1
    red_flowers_total = 12 # 12 red flowers
    red_pick_percent_text = 50 # 50% of the red roses
    percent_factor = 0.01 # WK
    picked_red_roses = red_flowers_total * red_pick_percent_text * percent_factor

    # L2
    pink_flowers_total = 18 # 18 pink flowers
    pink_pick_percent_text = 50 # 50% pink roses
    picked_pink_roses = pink_flowers_total * pink_pick_percent_text * percent_factor

    # L3
    yellow_flowers_total = 20 # 20 yellow flowers
    yellow_pick_percent_text = 25 # 25% of the yellow roses
    picked_yellow_roses = yellow_flowers_total * yellow_pick_percent_text * percent_factor

    # L4
    orange_flowers_total = 8 # 8 orange flowers
    orange_pick_percent_text = 25 # 25% orange roses
    picked_orange_roses = orange_flowers_total * orange_pick_percent_text * percent_factor

    # L5
    total_roses = picked_red_roses + picked_pink_roses + picked_yellow_roses + picked_orange_roses

    # FA
    answer = total_roses
    return answer
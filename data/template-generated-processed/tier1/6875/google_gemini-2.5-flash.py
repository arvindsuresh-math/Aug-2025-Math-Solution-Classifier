def solve():
    """Index: 6875.
    Returns: the total ounces of fat Ellianna served.
    """
    # L1
    num_fish_each_type = 40 # 40 fish of each type
    herring_fat_oz = 40 # 40 oz of fat
    herring_total_fat = num_fish_each_type * herring_fat_oz

    # L2
    eel_fat_oz = 20 # 20 oz
    eel_total_fat = num_fish_each_type * eel_fat_oz

    # L3
    herring_eel_combined_fat = herring_total_fat + eel_total_fat

    # L4
    pike_more_than_eel = 10 # 10 more oz of fat than an eel
    pike_fat_oz = pike_more_than_eel + eel_fat_oz

    # L5
    pike_total_fat = num_fish_each_type * pike_fat_oz

    # L6
    total_fat_served = pike_total_fat + herring_eel_combined_fat

    # FA
    answer = total_fat_served
    return answer
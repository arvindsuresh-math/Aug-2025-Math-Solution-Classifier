def solve():
    """Index: 6119.
    Returns: the total pounds of food needed for the horses for 3 days.
    """
    # L1
    feedings_per_day = 2 # twice a day
    oats_per_feeding = 4 # 4 pounds of oats
    oats_per_horse_per_day = feedings_per_day * oats_per_feeding

    # L2
    num_days = 3 # for 3 days
    total_oats_per_horse = oats_per_horse_per_day * num_days

    # L3
    num_horses = 4 # four horses
    total_oats_all_horses = total_oats_per_horse * num_horses

    # L4
    grain_per_feeding = 3 # 3 pounds of grain
    total_grain_per_horse = grain_per_feeding * num_days

    # L5
    total_grain_all_horses = total_grain_per_horse * num_horses

    # L6
    total_food_needed = total_oats_all_horses + total_grain_all_horses

    # FA
    answer = total_food_needed
    return answer
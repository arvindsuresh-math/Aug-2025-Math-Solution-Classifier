def solve():
    """Index: 7283.
    Returns: the total number of plant beds the farmer had.
    """
    # L1
    bean_seedlings = 64 # 64 bean seedlings
    bean_seedlings_per_row = 8 # plants 8 seedlings in a row
    bean_rows = bean_seedlings / bean_seedlings_per_row

    # L2
    pumpkin_seeds = 84 # 84 pumpkin seeds
    pumpkin_seeds_per_row = 7 # plants 7 seeds in a row
    pumpkin_rows = pumpkin_seeds / pumpkin_seeds_per_row

    # L3
    radishes = 48 # 48 radishes
    radishes_per_row = 6 # 6 radishes in a row
    radish_rows = radishes / radishes_per_row

    # L4
    total_rows = bean_rows + pumpkin_rows + radish_rows

    # L5
    rows_per_plant_bed = 2 # two rows per plant bed
    total_plant_beds = total_rows / rows_per_plant_bed

    # FA
    answer = total_plant_beds
    return answer
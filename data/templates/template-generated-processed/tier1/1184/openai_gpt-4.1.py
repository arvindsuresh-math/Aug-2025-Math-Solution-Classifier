def solve():
    """Index: 1184.
    Returns: the total number of seeds Grace can plant in all four beds of her raised bed garden.
    """
    # L1
    rows_per_large_bed = 4 # 4 rows of lettuce
    seeds_per_row_large = 25 # 25 seeds being sown per row
    seeds_per_large_bed = rows_per_large_bed * seeds_per_row_large

    # L2
    num_large_beds = 2 # 2 large beds
    total_seeds_large = seeds_per_large_bed * num_large_beds

    # L3
    rows_per_medium_bed = 3 # 3 rows
    seeds_per_row_medium = 20 # 20 seeds being sown per row
    seeds_per_medium_bed = rows_per_medium_bed * seeds_per_row_medium

    # L4
    num_medium_beds = 2 # 2 medium beds
    total_seeds_medium = seeds_per_medium_bed * num_medium_beds

    # L5
    total_seeds = total_seeds_large + total_seeds_medium

    # FA
    answer = total_seeds
    return answer
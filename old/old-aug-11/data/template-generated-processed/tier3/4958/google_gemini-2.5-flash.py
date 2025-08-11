def solve():
    """Index: 4958.
    Returns: the number of daisies in each bouquet of daisies.
    """
    # L1
    rose_bouquets_sold = 10 # 10 of these were rose bouquets
    roses_per_bouquet = 12 # each contain 12 roses
    total_roses_sold = rose_bouquets_sold * roses_per_bouquet

    # L2
    total_flowers_sold = 190 # sold 190 flowers in total today
    total_daisies_sold = total_flowers_sold - total_roses_sold

    # L3
    daisy_bouquets_sold = 10 # the remaining 10 bouquets were daisy bouquets
    daisies_per_bouquet = total_daisies_sold / daisy_bouquets_sold

    # FA
    answer = daisies_per_bouquet
    return answer
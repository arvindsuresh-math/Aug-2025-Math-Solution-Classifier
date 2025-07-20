def solve():
    """Index: 5229.
    Returns: the number of bowlfuls of cereal in each box.
    """
    # L1
    clusters_per_spoonful = 4 # 4 clusters of oats
    spoonfuls_per_bowl = 25 # 25 spoonfuls of cereal
    clusters_per_bowl = clusters_per_spoonful * spoonfuls_per_bowl

    # L2
    clusters_per_box = 500 # 500 clusters of oats
    bowlfuls_per_box = clusters_per_box / clusters_per_bowl

    # FA
    answer = bowlfuls_per_box
    return answer
def solve():
    """Index: 5286.
    Returns: the total number of bouquets the florist can make.
    """
    # L1
    narcissus_flowers = 75 # 75 narcissus flowers
    flowers_per_bouquet = 5 # 5 flowers each
    bouquets_narcissus = narcissus_flowers / flowers_per_bouquet

    # L2
    chrysanthemums_flowers = 90 # 90 chrysanthemums
    bouquets_chrysanthemums = chrysanthemums_flowers / flowers_per_bouquet

    # L3
    total_bouquets = bouquets_narcissus + bouquets_chrysanthemums

    # FA
    answer = total_bouquets
    return answer
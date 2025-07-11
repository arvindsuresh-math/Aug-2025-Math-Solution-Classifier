def solve():
    """Index: 2902.
    Returns: the number of flowers in each basket.
    """
    # L1
    flowers_per_daughter = 5 # plant 5 flowers each
    num_daughters = 2 # Dane’s two daughters
    initial_flowers_planted = flowers_per_daughter * num_daughters

    # L2
    additional_flowers_grown = 20 # grew into 20 more
    total_flowers_after_growth = initial_flowers_planted + additional_flowers_grown

    # L3
    flowers_died = 10 # 10 of them died
    flowers_after_death = total_flowers_after_growth - flowers_died

    # L4
    num_baskets = 5 # split them between 5 different baskets
    flowers_per_basket = flowers_after_death / num_baskets

    # FA
    answer = flowers_per_basket
    return answer
def solve():
    """Index: 766.
    Returns: the number of meals that are neither kosher nor vegan.
    """
    # L1
    vegan_meals = 7 # 7 need vegan meals
    kosher_meals = 8 # 8 need kosher meals
    sum_vegan_kosher = vegan_meals + kosher_meals

    # L2
    both_vegan_kosher = 3 # three people need meals that are both vegan and kosher
    either_vegan_or_kosher = sum_vegan_kosher - both_vegan_kosher

    # L3
    total_clients = 30 # Out of her 30 clients
    neither_vegan_nor_kosher = total_clients - either_vegan_or_kosher

    # FA
    answer = neither_vegan_nor_kosher
    return answer
def solve():
    """Index: 766.
    Returns: the number of meals Megan delivers that are neither kosher nor vegan.
    """
    # L1
    vegan_clients = 7 # 7 need vegan meals
    kosher_clients = 8 # 8 need kosher meals
    sum_vegan_kosher = vegan_clients + kosher_clients

    # L2
    both_vegan_kosher = 3 # three people need meals that are both vegan and kosher
    total_special_meals = sum_vegan_kosher - both_vegan_kosher

    # L3
    total_clients = 30 # 30 clients
    neither_special_meals = total_clients - total_special_meals

    # FA
    answer = neither_special_meals
    return answer
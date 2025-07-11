def solve():
    """Index: 2571.
    Returns: the total number of eggs Eric will have collected.
    """
    # L1
    eggs_per_chicken_per_day = 3 # lay 3 eggs each day
    num_chickens = 4 # 4 chickens
    eggs_per_day = eggs_per_chicken_per_day * num_chickens

    # L2
    collection_days = 3 # after 3 days
    total_collected_eggs = eggs_per_day * collection_days

    # FA
    answer = total_collected_eggs
    return answer
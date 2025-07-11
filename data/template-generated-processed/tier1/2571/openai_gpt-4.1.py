def solve():
    """Index: 2571.
    Returns: the total number of eggs Eric will have collected after 3 days.
    """
    # L1
    eggs_per_chicken_per_day = 3 # chickens lay 3 eggs each day
    num_chickens = 4 # 4 chickens
    eggs_per_day = eggs_per_chicken_per_day * num_chickens

    # L2
    num_days = 3 # after 3 days
    total_eggs = eggs_per_day * num_days

    # FA
    answer = total_eggs
    return answer
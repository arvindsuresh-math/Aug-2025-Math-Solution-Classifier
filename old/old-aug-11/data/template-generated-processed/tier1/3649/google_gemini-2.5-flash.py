def solve():
    """Index: 3649.
    Returns: the total number of eggs Uncle Ben will have.
    """
    # L1
    total_chickens = 440 # 440 chickens
    num_roosters = 39 # 39 are roosters
    num_hens = total_chickens - num_roosters

    # L2
    hens_no_eggs = 15 # 15 of his hens do not lay eggs
    egg_laying_hens = num_hens - hens_no_eggs

    # L3
    eggs_per_hen = 3 # lays 3 eggs
    total_eggs = eggs_per_hen * egg_laying_hens

    # FA
    answer = total_eggs
    return answer
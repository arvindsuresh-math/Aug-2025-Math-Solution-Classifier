def solve():
    """Index: 6613.
    Returns: the number of egg-laying hens Mr. Curtis has on his farm.
    """
    # L1
    total_chickens = 325 # 325 chickens
    roosters = 28 # 28 are roosters
    total_hens = total_chickens - roosters

    # L2
    hens_not_laying = 20 # Twenty hens do not lay eggs
    egg_laying_hens = total_hens - hens_not_laying

    # FA
    answer = egg_laying_hens
    return answer
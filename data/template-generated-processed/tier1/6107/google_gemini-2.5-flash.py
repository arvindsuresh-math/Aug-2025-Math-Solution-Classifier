def solve():
    """Index: 6107.
    Returns: the total number of bushels needed to suffice the animals for a day.
    """
    # L1
    num_cows = 4 # 4 cows
    bushels_per_cow_sheep = 2 # eat 2 bushels a day
    bushels_for_cows = num_cows * bushels_per_cow_sheep

    # L2
    num_sheep = 3 # 3 sheep
    bushels_for_sheep = num_sheep * bushels_per_cow_sheep

    # L3
    num_chickens = 7 # 7 chickens
    bushels_per_chicken = 3 # eat 3 bushels a day
    bushels_for_chickens = num_chickens * bushels_per_chicken

    # L4
    total_bushels_needed = bushels_for_cows + bushels_for_sheep + bushels_for_chickens

    # FA
    answer = total_bushels_needed
    return answer
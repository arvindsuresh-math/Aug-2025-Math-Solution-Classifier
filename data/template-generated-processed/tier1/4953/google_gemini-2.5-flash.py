def solve():
    """Index: 4953.
    Returns: the number of cans of juice left to be loaded on the truck.
    """
    # L1
    total_cartons = 50 # 50 cartons that have been packed
    loaded_cartons = 40 # only 40 cartons have been loaded on a truck
    cartons_left = total_cartons - loaded_cartons

    # L2
    cans_per_carton = 20 # Each carton has 20 cans of juice
    cans_left = cartons_left * cans_per_carton

    # FA
    answer = cans_left
    return answer
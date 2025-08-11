def solve():
    """Index: 7075.
    Returns: the initial amount of sugar in grams.
    """
    # L1
    num_packs = 12 # 12 packs
    weight_per_pack = 250 # each pack weighs 250 grams
    total_packed_sugar = weight_per_pack * num_packs

    # L2
    sugar_left = 20 # has 20 grams of sugar left
    initial_sugar = total_packed_sugar + sugar_left

    # FA
    answer = initial_sugar
    return answer
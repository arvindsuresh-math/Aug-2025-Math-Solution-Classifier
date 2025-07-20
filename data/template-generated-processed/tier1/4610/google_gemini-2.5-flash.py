def solve():
    """Index: 4610.
    Returns: the total number of scoops of ice cream served.
    """
    # L1
    multiplier_double_cone = 2 # double cone
    scoops_per_single_cone = 1 # The cone has 1 scoop of ice cream
    double_cone_scoops = multiplier_double_cone * scoops_per_single_cone

    # L2
    multiplier_banana_split = 3 # 3 times as many scoops of ice cream as the cone
    banana_split_scoops = multiplier_banana_split * scoops_per_single_cone

    # L3
    waffle_bowl_extra_scoops = 1 # 1 more scoop than the banana split
    waffle_bowl_scoops = banana_split_scoops + waffle_bowl_extra_scoops

    # L4
    total_scoops = scoops_per_single_cone + double_cone_scoops + banana_split_scoops + waffle_bowl_scoops

    # FA
    answer = total_scoops
    return answer
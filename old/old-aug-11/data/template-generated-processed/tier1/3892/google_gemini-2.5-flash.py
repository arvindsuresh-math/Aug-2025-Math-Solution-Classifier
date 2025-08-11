def solve():
    """Index: 3892.
    Returns: the total weight of all the litter collected in pounds.
    """
    # L1
    neighborhood_multiplier = 82 # 82 times as much as Gina did by herself
    gina_bags = 2 # two bags of litter herself
    neighborhood_bags = neighborhood_multiplier * gina_bags

    # L2
    total_bags = neighborhood_bags + gina_bags

    # L3
    weight_per_bag = 4 # Each bag of litter weighs 4 pounds
    total_weight_pounds = total_bags * weight_per_bag

    # FA
    answer = total_weight_pounds
    return answer
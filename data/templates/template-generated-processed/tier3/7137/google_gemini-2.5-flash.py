def solve():
    """Index: 7137.
    Returns: the total weight of the remaining coconut macaroons.
    """
    # L1
    total_macaroons = 12 # John bakes 12 coconut macaroons
    num_bags = 4 # packs an equal number of the macaroons in 4 different brown bags
    macaroons_per_bag = total_macaroons / num_bags

    # L2
    remaining_macaroons = total_macaroons - macaroons_per_bag

    # L3
    weight_per_macaroon = 5 # each weighing 5 ounces
    total_weight = remaining_macaroons * weight_per_macaroon

    # FA
    answer = total_weight
    return answer
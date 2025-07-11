def solve():
    """Index: 569.
    Returns: the total amount of weight of Harry's custom creation.
    """
    # L1
    num_blue_weights = 4 # 4 blue weights
    blue_weight_per_unit = 2 # 2 pounds each
    total_blue_weight = num_blue_weights * blue_weight_per_unit

    # L2
    num_green_weights = 5 # 5 green weights
    green_weight_per_unit = 3 # 3 pounds each
    total_green_weight = num_green_weights * green_weight_per_unit

    # L3
    total_weights_only = total_blue_weight + total_green_weight

    # L4
    bar_weight = 2 # The bar itself weighs 2 pounds
    final_total_weight = total_weights_only + bar_weight

    # FA
    answer = final_total_weight
    return answer
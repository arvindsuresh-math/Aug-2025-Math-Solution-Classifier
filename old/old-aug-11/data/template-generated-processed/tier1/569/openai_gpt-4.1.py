def solve():
    """Index: 569.
    Returns: the total amount of weight, in pounds, of Harry's custom creation.
    """
    # L1
    num_blue = 4 # 4 blue weights
    blue_weight = 2 # blue weights are 2 pounds each
    blue_total = num_blue * blue_weight

    # L2
    num_green = 5 # 5 green weights
    green_weight = 3 # green weights are 3 pounds each
    green_total = num_green * green_weight

    # L3
    weights_total = blue_total + green_total

    # L4
    bar_weight = 2 # bar itself weighs 2 pounds
    total_weight = weights_total + bar_weight

    # FA
    answer = total_weight
    return answer
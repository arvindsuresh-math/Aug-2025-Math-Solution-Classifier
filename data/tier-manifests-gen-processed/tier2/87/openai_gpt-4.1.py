def solve():
    """Index: 87.
    Returns: how much more the cow is worth after gaining the weight.
    """
    # L1
    initial_weight = 400 # cow weighs 400 pounds
    weight_increase_factor = 1.5 # increased its weight to 1.5 times its starting weight
    final_weight = initial_weight * weight_increase_factor

    # L2
    weight_gain = final_weight - initial_weight

    # L3
    price_per_pound = 3 # $3 per pound
    value_increase = weight_gain * price_per_pound

    # FA
    answer = value_increase
    return answer
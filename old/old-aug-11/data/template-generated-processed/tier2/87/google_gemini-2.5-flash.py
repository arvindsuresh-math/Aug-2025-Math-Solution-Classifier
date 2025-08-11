def solve():
    """Index: 87.
    Returns: how much more the cow is worth after gaining weight.
    """
    # L1
    initial_weight = 400 # John's cow weighs 400 pounds
    weight_increase_factor = 1.5 # increased its weight to 1.5 times its starting weight
    new_weight = initial_weight * weight_increase_factor

    # L2
    weight_gained = new_weight - initial_weight

    # L3
    price_per_pound = 3 # sell the cow for $3 per pound
    value_increase = weight_gained * price_per_pound

    # FA
    answer = value_increase
    return answer
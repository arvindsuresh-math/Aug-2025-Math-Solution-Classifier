def solve(
    initial_weight: float = 400,  # John's cow weighs 400 pounds
    weight_multiplier: float = 1.5,  # increased its weight to 1.5 times its starting weight
    price_per_pound: float = 3  # He is able to sell the cow for $3 per pound
):
    """Index: 87.
    Returns: the increase in the cow's value after gaining weight.
    """

    #: L1
    new_weight = initial_weight * weight_multiplier

    #: L2
    weight_gain = new_weight - initial_weight

    #: L3
    value_increase = new_weight * price_per_pound

    #: FA
    answer = value_increase
    return answer
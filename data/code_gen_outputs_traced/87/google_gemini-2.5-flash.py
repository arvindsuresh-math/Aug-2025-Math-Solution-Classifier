def solve(
        initial_weight: int = 400, # John's cow weighs 400 pounds
        weight_multiplier: float = 1.5, # It increased its weight to 1.5 times its starting weight
        price_per_pound: int = 3 # He is able to sell the cow for $3 per pound
    ):
    """Index: 87.
    Returns: how much more the cow is worth after gaining the weight.
    """

    #: L1
    final_weight = initial_weight * weight_multiplier # eval: 600.0 = 400 * 1.5

    #: L2
    weight_gained = final_weight - initial_weight # eval: 200.0 = 600.0 - 400

    #: L3
    increased_value = weight_gained * price_per_pound # eval: 600.0 = 200.0 * 3

    #: FA
    answer = increased_value # eval: 600.0 = 600.0
    return answer # eval: return 600.0

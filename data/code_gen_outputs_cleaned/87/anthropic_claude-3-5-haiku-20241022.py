def solve(
    initial_weight: int = 400,  # John's cow weighs 400 pounds
    weight_increase_factor: float = 1.5,  # It increased its weight to 1.5 times its starting weight
    price_per_pound: int = 3  # He is able to sell the cow for $3 per pound
):
    """Index: 87.
    Returns: the additional value of the cow after weight gain.
    """
    #: L1
    final_weight = initial_weight * weight_increase_factor

    #: L2
    weight_gained = final_weight - initial_weight

    #: L3
    value_increase = weight_gained * price_per_pound

    answer = value_increase  # FINAL ANSWER
    return answer
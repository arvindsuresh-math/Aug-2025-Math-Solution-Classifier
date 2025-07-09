def solve(
    initial_weight: int = 400,  # John's cow weighs 400 pounds
    weight_increase_factor: float = 1.5,  # It increased its weight to 1.5 times its starting weight
    price_per_pound: int = 3  # He is able to sell the cow for $3 per pound
):
    """Index: 87.
    Returns: the additional value of the cow after weight gain.
    """

    #: L1
    final_weight = weight_increase_factor * weight_increase_factor # eval: 2.25 = 1.5 * 1.5

    #: L2
    weight_gained = final_weight - initial_weight # eval: -397.75 = 2.25 - 400

    #: L3
    value_increase = weight_gained * price_per_pound # eval: -1193.25 = -397.75 * 3

    #: FA
    answer = value_increase
    return answer # eval: return -1193.25

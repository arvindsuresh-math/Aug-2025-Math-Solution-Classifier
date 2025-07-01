def solve(
    starting_weight: int = 400, # John's cow weighs 400 pounds
    weight_increase_factor: float = 1.5, # It increased its weight to 1.5 times its starting weight
    price_per_pound: int = 3 # He is able to sell the cow for $3 per pound
):
    """Index: 87.
    Returns: the increase in the cow's value after gaining weight.
    """

    #: L1
    new_weight = starting_weight * weight_increase_factor # eval: 600.0 = 400 * 1.5

    #: L2

    #: L3
    value_increase = weight_increase_factor * price_per_pound # eval: 4.5 = 1.5 * 3

    #: FA
    answer = value_increase
    return answer # eval: return 4.5

def solve(
    total_weight_needed: int = 1000  # bear needs to gain 1000 pounds
):
    """Index: 61.
    Returns: the pounds gained by the bear eating small animals.
    """

    #: L1
    weight_from_berries = 190.0 # eval: 190.0 = 190.0

    #: L2
    weight_from_acorns = 2 * weight_from_berries # eval: 380.0 = 2 * 190.0

    #: L3
    remaining_weight_needed = total_weight_needed - weight_from_berries - weight_from_acorns # eval: 430.0 = 1000 - 190.0 - 380.0

    #: L4
    weight_from_salmon = remaining_weight_needed / 2 # eval: 215.0 = 430.0 / 2

    #: L5
    weight_from_small_animals = remaining_weight_needed - weight_from_salmon # eval: 215.0 = 430.0 - 215.0

    #: FA
    answer = weight_from_small_animals
    return answer # eval: return 215.0

def solve(
    total_weight_needed: int = 1000  # bear needs to gain 1000 pounds
):
    """Index: 61.
    Returns: the pounds gained by the bear eating small animals.
    """

    #: L1

    #: L2
    weight_from_acorns = 2 * total_weight_needed # eval: 2000 = 2 * 1000

    #: L3
    remaining_weight_needed = total_weight_needed - total_weight_needed - weight_from_acorns # eval: -2000 = 1000 - 1000 - 2000

    #: L4
    weight_from_salmon = remaining_weight_needed / 2 # eval: -1000.0 = -2000 / 2

    #: L5
    weight_from_small_animals = remaining_weight_needed - weight_from_salmon # eval: -1000.0 = -2000 - -1000.0

    #: FA
    answer = weight_from_small_animals
    return answer # eval: return -1000.0

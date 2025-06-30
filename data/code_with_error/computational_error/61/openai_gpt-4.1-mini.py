def solve(
    total_weight_needed: int = 1000  # bear needs to gain 1000 pounds
):
    """Index: 61.
    Returns: the pounds gained by the bear eating small animals.
    """

    #: L1
    weight_from_berries = 190.0

    #: L2
    weight_from_acorns = 2 * weight_from_berries

    #: L3
    remaining_weight_needed = total_weight_needed - weight_from_berries - weight_from_acorns

    #: L4
    weight_from_salmon = remaining_weight_needed / 2

    #: L5
    weight_from_small_animals = remaining_weight_needed - weight_from_salmon

    #: FA
    answer = weight_from_small_animals
    return answer
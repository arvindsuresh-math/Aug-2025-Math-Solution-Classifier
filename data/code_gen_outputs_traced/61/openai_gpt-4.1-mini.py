def solve(
    total_weight_needed: int = 1000  # bear needs to gain 1000 pounds
):
    """Index: 61.
    Returns: the pounds gained by the bear eating small animals.
    """
    #: L1
    weight_from_berries = (1/5) * total_weight_needed # eval: 200.0 = (1/5) * 1000
    #: L2
    weight_from_acorns = 2 * weight_from_berries # eval: 400.0 = 2 * 200.0
    #: L3
    remaining_weight_needed = total_weight_needed - weight_from_berries - weight_from_acorns # eval: 400.0 = 1000 - 200.0 - 400.0
    #: L4
    weight_from_salmon = remaining_weight_needed / 2 # eval: 200.0 = 400.0 / 2
    #: L5
    weight_from_small_animals = remaining_weight_needed - weight_from_salmon # eval: 200.0 = 400.0 - 200.0
    answer = weight_from_small_animals  # FINAL ANSWER # eval: 200.0 = 200.0  # FINAL ANSWER
    return answer # eval: return 200.0
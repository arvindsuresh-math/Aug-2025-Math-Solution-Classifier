def solve():
    """Index: 61.
    Returns: the pounds gained from eating small animals.
    """
    # L1
    total_weight_needed = 1000 # needs to gain 1000 pounds
    berry_fraction_numerator = 1 # a fifth of the weight
    berry_fraction_denominator = 5 # a fifth of the weight
    weight_from_berries = berry_fraction_numerator / berry_fraction_denominator * total_weight_needed

    # L2
    acorn_multiplier = 2 # twice that amount from acorns
    weight_from_acorns = acorn_multiplier * weight_from_berries

    # L3
    remaining_weight_after_berries_acorns = total_weight_needed - weight_from_berries - weight_from_acorns

    # L4
    salmon_divisor = 2 # half of the remaining weight
    weight_from_salmon = remaining_weight_after_berries_acorns / salmon_divisor

    # L5
    weight_from_small_animals = remaining_weight_after_berries_acorns - weight_from_salmon

    # FA
    answer = weight_from_small_animals
    return answer
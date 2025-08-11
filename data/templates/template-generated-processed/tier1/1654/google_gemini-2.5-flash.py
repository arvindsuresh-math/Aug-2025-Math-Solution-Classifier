def solve():
    """Index: 1654.
    Returns: the total length of fencing Bob needs.
    """
    # L1
    garden_length = 225 # 225 feet long
    garden_width = 125 # 125 feet wide
    two_multiplier = 2 # WK
    length_contribution = two_multiplier * garden_length
    width_contribution = two_multiplier * garden_width
    perimeter = length_contribution + width_contribution

    # L2
    small_gate_width = 3 # 3-foot wide gate
    large_gate_width = 10 # 10-foot wide gate
    fencing_needed = perimeter - small_gate_width - large_gate_width

    # FA
    answer = fencing_needed
    return answer
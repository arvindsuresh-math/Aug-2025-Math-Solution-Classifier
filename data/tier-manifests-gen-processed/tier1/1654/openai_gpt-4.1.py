def solve():
    """Index: 1654.
    Returns: the total length of fencing Bob needs for his garden, accounting for the two gates.
    """
    # L1
    length = 225 # 225 feet long
    width = 125 # 125 feet wide
    perimeter = 2 * length + 2 * width

    # L2
    small_gate = 3 # 3-foot wide gate
    large_gate = 10 # 10-foot wide gate
    fencing_needed = perimeter - small_gate - large_gate

    # FA
    answer = fencing_needed
    return answer
def solve():
    """Index: 6737.
    Returns: the depth of Northton's time capsule.
    """
    # L1
    southton_depth = 15 # 15 feet underground
    multiplier = 4 # 4 times the depth
    multiplied_depth = southton_depth * multiplier

    # L2
    depth_offset = 12 # 12 feet higher
    northton_depth = multiplied_depth - depth_offset

    # FA
    answer = northton_depth
    return answer
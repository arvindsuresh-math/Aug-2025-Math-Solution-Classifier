def solve():
    """Index: 6387.
    Returns: the uncovered area of the floor.
    """
    # L1
    floor_length = 10 # 10 m long
    floor_width = 8 # 8 m wide
    floor_area = floor_length * floor_width

    # L2
    carpet_side = 4 # 4 m sides
    carpet_area = carpet_side * carpet_side

    # L3
    uncovered_area = floor_area - carpet_area

    # FA
    answer = uncovered_area
    return answer
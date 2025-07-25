def solve():
    """Index: 7329.
    Returns: the number of square inches of the box left uncovered.
    """
    # L1
    box_height = 4 # 4 inches tall
    box_width = 6 # 6 inches wide
    shoebox_area = box_height * box_width

    # L2
    block_side = 4 # 4 inches per side
    block_area = block_side * block_side

    # L3
    uncovered_area = shoebox_area - block_area

    # FA
    answer = uncovered_area
    return answer
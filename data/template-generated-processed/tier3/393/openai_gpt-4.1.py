def solve():
    """Index: 393.
    Returns: the width of the sandbox in feet.
    """
    # L1
    perimeter = 30 # the perimeter of the sandbox is 30 feet
    # width is W, length is 2W
    # L2
    total_W_coefficient = 6 # W + W + 2W + 2W = 6W
    # L3
    width = perimeter / total_W_coefficient
    # FA
    answer = width
    return answer
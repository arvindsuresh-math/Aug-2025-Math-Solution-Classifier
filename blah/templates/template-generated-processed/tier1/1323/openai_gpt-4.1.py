def solve():
    """Index: 1323.
    Returns: the length of each side of the square quilt using all the fabric.
    """
    # L1
    width = 6 # 6 feet
    length = 24 # 24 feet
    area = width * length

    # L2
    side = area ** 0.5

    # FA
    answer = side
    return answer
def solve():
    """Index: 2185.
    Returns: the total number of flowers at the Greene Nursery.
    """
    # L1
    red_roses = 1491 # 1491 red roses
    yellow_carnations = 3025 # 3025 yellow carnations
    sum_roses_carnations = red_roses + yellow_carnations

    # L2
    white_roses = 1768 # 1768 white roses
    total_flowers = sum_roses_carnations + white_roses

    # FA
    answer = total_flowers
    return answer
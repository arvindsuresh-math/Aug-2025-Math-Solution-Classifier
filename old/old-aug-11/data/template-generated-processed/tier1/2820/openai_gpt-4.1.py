def solve():
    """Index: 2820.
    Returns: the total number of spots on the cow.
    """
    # L1
    left_spots = 16 # 16 spots on its left side
    multiplier = 3 # three times that number
    right_spots_times = left_spots * multiplier

    # L2
    right_spots_add = 7 # plus 7 on its right side
    right_spots = right_spots_times + right_spots_add

    # L3
    total_spots = right_spots + left_spots

    # FA
    answer = total_spots
    return answer
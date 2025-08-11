def solve():
    """Index: 2820.
    Returns: the total number of spots on the cow.
    """
    # L1
    spots_left_side = 16 # 16 spots on its left side
    multiplier = 3 # three times that number
    spots_left_times_three = spots_left_side * multiplier

    # L2
    additional_spots_right = 7 # plus 7 on its right side
    spots_right_side = spots_left_times_three + additional_spots_right

    # L3
    total_spots = spots_right_side + spots_left_side

    # FA
    answer = total_spots
    return answer
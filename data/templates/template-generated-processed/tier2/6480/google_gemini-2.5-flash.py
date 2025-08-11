def solve():
    """Index: 6480.
    Returns: the number of mugs of another color than mentioned.
    """
    # L1
    yellow_mugs = 12 # 12 yellow mugs
    red_mugs_factor = 0.5 # half as many red mugs
    red_mugs = yellow_mugs * red_mugs_factor

    # L2
    blue_mugs_factor = 3 # three times more blue mugs
    blue_mugs = blue_mugs_factor * red_mugs

    # L3
    total_mugs = 40 # 40 different mugs
    other_color_mugs = total_mugs - blue_mugs - red_mugs - yellow_mugs

    # FA
    answer = other_color_mugs
    return answer
def solve():
    """Index: 2621.
    Returns: the total number of colored hangers in Fifi's closet.
    """
    # L1
    green_hangers = 4 # 4 green hangers
    blue_less_than_green = 1 # one less blue hanger than there are green hangers
    blue_hangers = green_hangers - blue_less_than_green

    # L2
    yellow_less_than_blue = 1 # one less yellow hanger than there are blue hangers
    yellow_hangers = blue_hangers - yellow_less_than_blue

    # L3
    pink_hangers = 7 # 7 pink hangers
    total_hangers = pink_hangers + green_hangers + blue_hangers + yellow_hangers

    # FA
    answer = total_hangers
    return answer
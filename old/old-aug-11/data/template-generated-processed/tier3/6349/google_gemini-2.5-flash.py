def solve():
    """Index: 6349.
    Returns: the total number of houses that are not yellow.
    """
    # L1
    green_houses = 90 # 90 green houses
    green_yellow_multiplier = 3 # three times as many green houses as yellow houses
    yellow_houses = green_houses / green_yellow_multiplier

    # L2
    yellow_house_difference = 40 # 40 fewer yellow houses than red houses
    blue_houses = yellow_houses + yellow_house_difference

    # L3
    houses_not_yellow = blue_houses + green_houses

    # FA
    answer = houses_not_yellow
    return answer
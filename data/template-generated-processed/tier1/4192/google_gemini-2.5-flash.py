def solve():
    """Index: 4192.
    Returns: the total number of chairs in Susan's house.
    """
    # L1
    red_chairs = 5 # 5 red chairs
    yellow_multiplier = 4 # 4 times as many yellow chairs as red chairs
    yellow_chairs = red_chairs * yellow_multiplier

    # L2
    blue_fewer_than_yellow = 2 # 2 fewer blue chairs than yellow chairs
    blue_chairs = yellow_chairs - blue_fewer_than_yellow

    # L3
    total_chairs = red_chairs + yellow_chairs + blue_chairs

    # FA
    answer = total_chairs
    return answer
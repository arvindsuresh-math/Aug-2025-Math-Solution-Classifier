def solve():
    """Index: 7253.
    Returns: the number of chairs left in Rodrigo's classroom.
    """
    # L1
    red_chairs = 4 # 4 red chairs
    multiplier_yellow_red = 2 # 2 times as many yellow chairs as red chairs
    yellow_chairs = multiplier_yellow_red * red_chairs

    # L2
    fewer_blue_than_yellow = 2 # 2 fewer blue chairs than yellow chairs
    blue_chairs = yellow_chairs - fewer_blue_than_yellow

    # L3
    total_chairs_morning = red_chairs + yellow_chairs + blue_chairs

    # L4
    lisa_borrows = 3 # Lisa borrows 3 chairs
    chairs_remaining = total_chairs_morning - lisa_borrows

    # FA
    answer = chairs_remaining
    return answer
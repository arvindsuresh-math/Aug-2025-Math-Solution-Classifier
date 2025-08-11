def solve():
    """Index: 7244.
    Returns: the total number of buttons the tailor purchased.
    """
    # L1
    green_buttons = 90 # 90 green buttons
    more_yellow_than_green = 10 # 10 more yellow buttons than the green buttons
    yellow_buttons = green_buttons + more_yellow_than_green

    # L2
    fewer_blue_than_green = 5 # 5 fewer blue buttons than the green buttons
    blue_buttons = green_buttons - fewer_blue_than_green

    # L3
    total_buttons = green_buttons + yellow_buttons + blue_buttons

    # FA
    answer = total_buttons
    return answer
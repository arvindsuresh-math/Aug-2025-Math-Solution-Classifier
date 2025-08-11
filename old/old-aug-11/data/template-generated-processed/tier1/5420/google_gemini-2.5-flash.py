def solve():
    """Index: 5420.
    Returns: the number of more red marbles than yellow marbles.
    """
    # L1
    total_marbles = 19 # 19 marbles in a bowl
    yellow_marbles = 5 # 5 of which are yellow
    remainder_marbles = total_marbles - yellow_marbles

    # L2
    blue_ratio_part = 3 # ratio 3:4
    red_ratio_part = 4 # ratio 3:4
    share_value = remainder_marbles / (blue_ratio_part + red_ratio_part)

    # L3
    red_marbles = red_ratio_part * share_value

    # L4
    difference_red_yellow = red_marbles - yellow_marbles

    # FA
    answer = difference_red_yellow
    return answer
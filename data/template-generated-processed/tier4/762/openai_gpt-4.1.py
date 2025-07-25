def solve():
    """Index: 762.
    Returns: the number of pens left for Lenny.
    """
    # L1
    num_boxes = 20 # 20 boxes of pens
    pens_per_box = 5 # Each box contained 5 pens
    total_pens = num_boxes * pens_per_box

    # L2
    close_friends_percent_num = 40 # 40% of the pens to her close friends
    percent_factor = 0.01 # WK
    pens_given_friends = total_pens * close_friends_percent_num * percent_factor

    # L3
    pens_after_friends = total_pens - pens_given_friends

    # L4
    classmates_fraction_denom = 4 # one-fourth of what's left to her classmates
    pens_given_classmates = pens_after_friends / classmates_fraction_denom

    # L5
    pens_left = pens_after_friends - pens_given_classmates

    # FA
    answer = pens_left
    return answer
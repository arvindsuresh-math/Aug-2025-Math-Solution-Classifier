def solve():
    """Index: 762.
    Returns: the number of pens left for Lenny.
    """
    # L1
    num_boxes = 20 # 20 boxes of pens
    pens_per_box = 5 # Each box contained 5 pens
    total_pens = num_boxes * pens_per_box

    # L2
    percent_to_friends_num = 40 # 40% of the pens
    percent_factor = 0.01 # WK
    pens_to_friends = total_pens * percent_to_friends_num * percent_factor

    # L3
    pens_after_friends = total_pens - pens_to_friends

    # L4
    fraction_to_classmates_divisor = 4 # one-fourth of what's left
    pens_to_classmates = pens_after_friends / fraction_to_classmates_divisor

    # L5
    pens_left_for_lenny = pens_after_friends - pens_to_classmates

    # FA
    answer = pens_left_for_lenny
    return answer
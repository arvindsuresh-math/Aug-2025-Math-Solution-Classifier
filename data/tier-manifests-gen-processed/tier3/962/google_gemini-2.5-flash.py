def solve():
    """Index: 962.
    Returns: the number of biscuits Unique can make.
    """
    # L1
    dough_length = 12 # 12 inches by 12 inches
    dough_width = 12 # 12 inches by 12 inches
    total_dough_area = dough_length * dough_width

    # L2
    biscuit_side_length = 3 # 3 inches by 3 inches
    biscuit_side_width = 3 # 3 inches by 3 inches
    biscuit_area = biscuit_side_length * biscuit_side_width

    # L3
    number_of_biscuits = total_dough_area / biscuit_area

    # FA
    answer = number_of_biscuits
    return answer
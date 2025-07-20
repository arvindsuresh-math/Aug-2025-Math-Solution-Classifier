def solve():
    """Index: 4420.
    Returns: the number of pencils Steve has left.
    """
    # L1
    num_boxes = 2 # 2 boxes of pencils
    pencils_per_box = 12 # 12 pencils in each box
    initial_pencils = num_boxes * pencils_per_box

    # L2
    pencils_given_to_lauren = 6 # gave 6 pencils to Lauren
    matt_more_than_lauren = 3 # gave Matt 3 more pencils than he gave to Lauren
    pencils_given_to_matt = pencils_given_to_lauren + matt_more_than_lauren

    # L3
    pencils_left = initial_pencils - pencils_given_to_matt - pencils_given_to_lauren

    # FA
    answer = pencils_left
    return answer
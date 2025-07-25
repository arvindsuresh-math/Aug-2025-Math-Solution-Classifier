def solve():
    """Index: 5736.
    Returns: the number of pencils Ashton had left.
    """
    # L1
    num_boxes = 2 # two boxes of pencils
    pencils_per_box = 14 # fourteen pencils in each box
    initial_pencils = num_boxes * pencils_per_box

    # L2
    given_away = 6 # gave six pencils to his brother
    pencils_left = initial_pencils - given_away

    # FA
    answer = pencils_left
    return answer
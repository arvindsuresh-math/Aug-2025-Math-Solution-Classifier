def solve():
    """Index: 1874.
    Returns: the number of boxes of cookies left for Sonny.
    """
    # L1
    given_to_brother = 12 # gave 12 to his brother
    given_to_sister = 9 # 9 to his sister
    given_to_cousin = 7 # gave 7 to his cousin
    total_given_away = given_to_brother + given_to_sister + given_to_cousin

    # L2
    initial_boxes = 45 # received 45 boxes of cookies
    boxes_left = initial_boxes - total_given_away

    # FA
    answer = boxes_left
    return answer
def solve():
    """Index: 1874.
    Returns: the number of boxes of cookies left for Sonny.
    """
    # L1
    gave_brother = 12 # gave 12 to his brother
    gave_sister = 9 # 9 to his sister
    gave_cousin = 7 # he gave 7 to his cousin
    total_given = gave_brother + gave_sister + gave_cousin

    # L2
    total_received = 45 # Sonny received 45 boxes of cookies
    boxes_left = total_received - total_given

    # FA
    answer = boxes_left
    return answer
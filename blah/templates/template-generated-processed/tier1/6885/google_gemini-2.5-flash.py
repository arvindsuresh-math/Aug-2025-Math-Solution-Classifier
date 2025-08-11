def solve():
    """Index: 6885.
    Returns: the total number of match sticks that Farah ordered.
    """
    # L1
    num_boxes = 4 # 4 boxes
    matchboxes_per_box = 20 # 20 matchboxes each
    total_matchboxes = num_boxes * matchboxes_per_box

    # L2
    sticks_per_matchbox = 300 # 300 sticks
    total_match_sticks = sticks_per_matchbox * total_matchboxes

    # FA
    answer = total_match_sticks
    return answer
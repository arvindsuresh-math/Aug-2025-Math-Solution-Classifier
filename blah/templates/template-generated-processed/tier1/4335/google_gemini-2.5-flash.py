def solve():
    """Index: 4335.
    Returns: the total number of matches James has.
    """
    # L1
    num_dozen_boxes = 5 # 5 dozen boxes of matches
    dozen = 12 # WK
    total_boxes = num_dozen_boxes * dozen

    # L2
    matches_per_box = 20 # Each box contains 20 matches
    total_matches = total_boxes * matches_per_box

    # FA
    answer = total_matches
    return answer
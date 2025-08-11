def solve():
    """Index: 6823.
    Returns: the number of new boxes Mr. Smith bought.
    """
    # L1
    total_markers_now = 86 # Now, he has 86 markers
    initial_markers = 32 # Mr. Smith had 32 markers
    markers_bought = total_markers_now - initial_markers

    # L2
    markers_per_box = 9 # have 9 markers in each box
    new_boxes = markers_bought / markers_per_box

    # FA
    answer = new_boxes
    return answer
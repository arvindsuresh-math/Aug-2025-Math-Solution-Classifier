def solve():
    """Index: 5998.
    Returns: the number of circles Ernie can make.
    """
    # L1
    ali_circles = 5 # Ali makes 5 circles
    boxes_per_ali_circle = 8 # Ali used 8 boxes to make each of his circles
    ali_boxes_used = ali_circles * boxes_per_ali_circle

    # L2
    initial_boxes = 80 # they had 80 boxes to begin with
    remaining_boxes = initial_boxes - ali_boxes_used

    # L3
    boxes_per_ernie_circle = 10 # Ernie used 10 for his
    ernie_circles_made = remaining_boxes / boxes_per_ernie_circle

    # FA
    answer = ernie_circles_made
    return answer
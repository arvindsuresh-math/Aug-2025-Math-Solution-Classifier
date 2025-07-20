def solve():
    """Index: 6997.
    Returns: the number of boxes Kim sold on Tuesday.
    """
    # L1
    thursday_boxes = 1200 # Kim sold 1200 boxes of cupcakes on Thursday
    multiplier_wednesday = 2 # twice as many boxes on Wednesday as she did on Thursday
    wednesday_boxes = thursday_boxes * multiplier_wednesday

    # L2
    multiplier_tuesday = 2 # twice as many boxes on Tuesday as she did on Wednesday
    tuesday_boxes = wednesday_boxes * multiplier_tuesday

    # FA
    answer = tuesday_boxes
    return answer
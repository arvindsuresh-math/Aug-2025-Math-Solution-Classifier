def solve():
    """Index: 3653.
    Returns: the number of decorations Mrs. Jackson gave to her neighbor.
    """
    # L1
    num_boxes = 4 # four boxes of Christmas decorations
    decorations_per_box = 15 # 15 decorations in each box
    total_decorations = num_boxes * decorations_per_box

    # L2
    used_decorations = 35 # only able to use 35 decorations
    given_decorations = total_decorations - used_decorations

    # FA
    answer = given_decorations
    return answer
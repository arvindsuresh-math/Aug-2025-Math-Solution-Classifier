def solve():
    """Index: 3889.
    Returns: the total number of boxes Louise needs.
    """
    # L1
    red_pencils = 20 # 20 red pencils
    blue_multiplier = 2 # twice as many blue pencils
    blue_pencils = red_pencils * blue_multiplier

    # L2
    green_pencils = red_pencils + blue_pencils

    # L3
    yellow_pencils = 40 # 40 yellow pencils
    total_pencils = red_pencils + blue_pencils + green_pencils + yellow_pencils

    # L4
    pencils_per_box = 20 # Each box holds 20 pencils each
    num_boxes = total_pencils / pencils_per_box

    # FA
    answer = num_boxes
    return answer
def solve():
    """Index: 1393.
    Returns: the number of jars of jam Cassy will have left when all the boxes are full.
    """
    # L1
    jars_per_box_1 = 12 # packs 12 jars of jam in 10 boxes
    num_boxes_1 = 10 # 10 boxes
    packed_1 = jars_per_box_1 * num_boxes_1

    # L2
    jars_per_box_2 = 10 # packs 10 jars of jam in 30 boxes
    num_boxes_2 = 30 # 30 boxes
    packed_2 = jars_per_box_2 * num_boxes_2

    # L3
    total_packed = packed_2 + packed_1

    # L4
    total_jars = 500 # she has 500 jars of jams
    jars_left = total_jars - total_packed

    # FA
    answer = jars_left
    return answer
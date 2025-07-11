def solve():
    """Index: 1393.
    Returns: the number of jars of jam left unpacked.
    """
    # L1
    jars_per_box_set1 = 12 # 12 jars of jam
    num_boxes_set1 = 10 # 10 boxes
    jars_packed_set1 = jars_per_box_set1 * num_boxes_set1

    # L2
    jars_per_box_set2 = 10 # 10 jars of jam
    num_boxes_set2 = 30 # 30 boxes
    jars_packed_set2 = jars_per_box_set2 * num_boxes_set2

    # L3
    total_jars_packed = jars_packed_set2 + jars_packed_set1

    # L4
    total_jars_available = 500 # 500 jars of jams
    jars_left_unpacked = total_jars_available - total_jars_packed

    # FA
    answer = jars_left_unpacked
    return answer
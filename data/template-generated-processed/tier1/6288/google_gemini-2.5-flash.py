def solve():
    """Index: 6288.
    Returns: the number of additional plates Alice was able to add before the tower fell.
    """
    # L1
    initial_plates = 27 # 27 plates on top of each other
    added_plates_first_batch = 37 # adds 37 more plates
    plates_stacked_initially = initial_plates + added_plates_first_batch

    # L2
    total_plates_at_crash = 83 # all 83 plates
    additional_plates_before_crash = total_plates_at_crash - plates_stacked_initially

    # FA
    answer = additional_plates_before_crash
    return answer
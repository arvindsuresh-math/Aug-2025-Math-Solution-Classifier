def solve():
    """Index: 3149.
    Returns: the number of meters of ribbon not used.
    """
    # L1
    total_ribbon_length = 30 # 30 meters ribbon
    num_equal_parts = 6 # 6 equal parts
    length_per_part = total_ribbon_length / num_equal_parts

    # L2
    parts_used = 4 # used 4 parts
    ribbon_used = length_per_part * parts_used

    # L3
    ribbon_not_used = total_ribbon_length - ribbon_used

    # FA
    answer = ribbon_not_used
    return answer
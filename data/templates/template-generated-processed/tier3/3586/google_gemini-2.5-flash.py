def solve():
    """Index: 3586.
    Returns: the number of meters of wire not used.
    """
    # L1
    total_wire_length = 50 # Ernest bought 50 meters of wire
    num_parts = 5 # cut it into 5 equal parts
    length_per_part = total_wire_length / num_parts

    # L2
    parts_used = 3 # used 3 parts of the wire
    wire_used = length_per_part * parts_used

    # L3
    wire_not_used = total_wire_length - wire_used

    # FA
    answer = wire_not_used
    return answer
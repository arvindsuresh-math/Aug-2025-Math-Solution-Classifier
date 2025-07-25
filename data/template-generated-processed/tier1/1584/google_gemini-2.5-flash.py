def solve():
    """Index: 1584.
    Returns: the total length of the entire show in minutes.
    """
    # L1
    third_segment_length = 10 # If the third segment is 10 minutes long
    second_segment_multiplier_to_third = 2 # the second segment is twice as long as the third
    second_segment_length = third_segment_length * second_segment_multiplier_to_third

    # L2
    first_segment_multiplier = 2 # The first interview segment is always twice as long as the other two segments combined
    first_segment_length = first_segment_multiplier * (third_segment_length + second_segment_length)

    # L3
    total_show_length = third_segment_length + second_segment_length + first_segment_length

    # FA
    answer = total_show_length
    return answer
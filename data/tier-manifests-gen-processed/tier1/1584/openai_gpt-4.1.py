def solve():
    """Index: 1584.
    Returns: the total length in minutes of the entire radio show.
    """
    # L1
    third_segment = 10 # the third segment is 10 minutes long
    second_segment = third_segment * 2

    # L2
    first_segment = 2 * (third_segment + second_segment)

    # L3
    total_length = third_segment + second_segment + first_segment

    # FA
    answer = total_length
    return answer
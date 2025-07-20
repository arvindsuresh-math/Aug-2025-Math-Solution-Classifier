def solve():
    """Index: 3319.
    Returns: the length of yarn used for crocheting.
    """
    # L1
    total_yarn_length = 10 # A 10 meters yarn
    num_parts = 5 # cut into 5 equal parts
    length_per_part = total_yarn_length / num_parts

    # L2
    parts_used = 3 # If 3 parts were used
    yarn_used_for_crocheting = length_per_part * parts_used

    # FA
    answer = yarn_used_for_crocheting
    return answer
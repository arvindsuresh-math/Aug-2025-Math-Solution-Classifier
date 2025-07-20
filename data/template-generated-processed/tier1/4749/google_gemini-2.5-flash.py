def solve():
    """Index: 4749.
    Returns: the number of bones Lassie started with before eating them on Saturday.
    """
    # L1
    end_bones = 35 # total of 35 bones
    received_bones = 10 # received 10 more bones
    bones_before_receiving = end_bones - received_bones

    # L2
    multiplier_for_half = 2 # half of her bones
    initial_bones = bones_before_receiving * multiplier_for_half

    # FA
    answer = initial_bones
    return answer
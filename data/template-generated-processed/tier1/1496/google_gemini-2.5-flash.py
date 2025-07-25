def solve():
    """Index: 1496.
    Returns: the number of bones Juniper has remaining.
    """
    # L1
    initial_bones = 4 # has 4 bones
    double_factor = 2 # double her number of bones
    bones_after_doubling = initial_bones * double_factor

    # L2
    stolen_bones = 2 # steals away two of Juniper's bones
    remaining_bones = bones_after_doubling - stolen_bones

    # FA
    answer = remaining_bones
    return answer
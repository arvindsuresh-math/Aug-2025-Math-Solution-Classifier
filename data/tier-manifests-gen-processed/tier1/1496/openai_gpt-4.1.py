def solve():
    """Index: 1496.
    Returns: the number of bones Juniper has remaining.
    """
    # L1
    initial_bones = 4 # Juniper ... has 4 bones
    double = 2 # double her number of bones
    after_doubling = initial_bones * double

    # L2
    bones_stolen = 2 # neighbor's dog steals away two of Juniper's bones
    bones_remaining = after_doubling - bones_stolen

    # FA
    answer = bones_remaining
    return answer
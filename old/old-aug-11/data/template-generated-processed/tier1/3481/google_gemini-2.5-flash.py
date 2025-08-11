def solve():
    """Index: 3481.
    Returns: the number of marbles Miriam started with.
    """
    # L1
    marbles_remaining = 30 # currently has 30 marbles
    given_to_brother = 60 # gave her brother 60 marbles
    marbles_before_brother = marbles_remaining + given_to_brother

    # L2
    multiplier_sister = 2 # twice that amount
    given_to_sister = multiplier_sister * given_to_brother

    # L3
    marbles_before_brother_sister = given_to_sister + marbles_before_brother

    # L4
    multiplier_savanna = 3 # three times the amount she currently has
    given_to_savanna = multiplier_savanna * marbles_remaining

    # L5
    total_marbles_start = marbles_before_brother_sister + given_to_savanna

    # FA
    answer = total_marbles_start
    return answer
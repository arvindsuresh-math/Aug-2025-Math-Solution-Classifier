def solve():
    """Index: 2806.
    Returns: the number of pounds of vegetables John used.
    """
    # L1
    initial_beef_pounds = 4 # 4 pounds of beef
    beef_left_out = 1 # all but 1 pound
    beef_used = initial_beef_pounds - beef_left_out

    # L2
    multiplier_for_vegetables = 2 # twice as many pounds of vegetables
    vegetables_used = beef_used * multiplier_for_vegetables

    # FA
    answer = vegetables_used
    return answer
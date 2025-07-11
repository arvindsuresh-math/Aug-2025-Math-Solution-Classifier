def solve():
    """Index: 2806.
    Returns: the number of pounds of vegetables John used.
    """
    # L1
    total_beef = 4 # John buys 4 pounds of beef
    beef_left = 1 # all but 1 pound in soup
    beef_used = total_beef - beef_left

    # L2
    veg_multiplier = 2 # twice as many pounds of vegetables as beef
    vegetables_used = beef_used * veg_multiplier

    # FA
    answer = vegetables_used
    return answer
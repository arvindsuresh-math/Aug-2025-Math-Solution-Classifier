def solve():
    """Index: 6994.
    Returns: the size Ginger wears.
    """
    # L1
    anna_size = 2 # size 2
    becky_multiplier = 3 # three times larger than Anna's
    becky_size = anna_size * becky_multiplier

    # L2
    ginger_multiplier = 2 # twice Becky's size
    temp_ginger_size = becky_size * ginger_multiplier

    # L3
    ginger_subtraction = 4 # minus 4
    ginger_size = temp_ginger_size - ginger_subtraction

    # FA
    answer = ginger_size
    return answer
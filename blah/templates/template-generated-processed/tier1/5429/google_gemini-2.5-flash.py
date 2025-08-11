def solve():
    """Index: 5429.
    Returns: the number of popsicle sticks Miss Davis has left.
    """
    # L1
    popsicle_sticks_per_group = 15 # 15 popsicle sticks to each of the 10 groups
    num_groups = 10 # 10 groups in her class
    total_given_out = popsicle_sticks_per_group * num_groups

    # L2
    initial_sticks = 170 # she had 170 popsicle sticks
    sticks_left = initial_sticks - total_given_out

    # FA
    answer = sticks_left
    return answer
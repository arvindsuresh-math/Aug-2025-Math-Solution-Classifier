def solve():
    """Index: 2390.
    Returns: the total number of blocks that fell down.
    """
    # L1
    first_stack = 7 # first stack was 7 blocks high
    second_higher_than_first = 5 # second stack was 5 block(s) higher than the first
    second_stack = first_stack + second_higher_than_first

    # L2
    third_higher_than_second = 7 # final stack was 7 block(s) higher than the second
    third_stack = second_stack + third_higher_than_second

    # L3
    second_left_standing = 2 # in the second tower she left 2 blocks standing
    second_knocked = second_stack - second_left_standing

    # L4
    third_left_standing = 3 # in the final tower she left 3 blocks standing
    third_knocked = third_stack - third_left_standing

    # L5
    total_knocked = first_stack + second_knocked + third_knocked

    # FA
    answer = total_knocked
    return answer
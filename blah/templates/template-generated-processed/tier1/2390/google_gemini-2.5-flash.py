def solve():
    """Index: 2390.
    Returns: the total number of blocks that fell down.
    """
    # L1
    first_stack_height = 7 # The first stack was 7 blocks high
    second_stack_higher_than_first = 5 # the second stack was 5 block(s) higher than the first
    second_stack_height = first_stack_height + second_stack_higher_than_first

    # L2
    third_stack_higher_than_second = 7 # the final stack was 7 block(s) higher than the second
    third_stack_height = second_stack_height + third_stack_higher_than_second

    # L3
    second_tower_left_standing = 2 # in the second tower she left 2 blocks standing
    second_tower_knocked_over = second_stack_height - second_tower_left_standing

    # L4
    final_tower_left_standing = 3 # in the final tower she left 3 blocks standing
    final_tower_knocked_over = third_stack_height - final_tower_left_standing

    # L5
    first_tower_knocked_over = 7 # knocked over the entire first tower (which was 7 blocks high)
    total_blocks_knocked_over = first_tower_knocked_over + second_tower_knocked_over + final_tower_knocked_over

    # FA
    answer = total_blocks_knocked_over
    return answer
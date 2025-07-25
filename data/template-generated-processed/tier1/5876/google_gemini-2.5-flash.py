def solve():
    """Index: 5876.
    Returns: the total number of blocks Thomas used in all.
    """
    # L1
    first_stack_height = 7 # The first stack was 7 blocks tall
    taller_than_first = 3 # The second stack was 3 blocks taller than the first
    second_stack_height = first_stack_height + taller_than_first

    # L2
    shorter_than_second = 6 # The third stack was 6 blocks shorter than the second stack
    third_stack_height = second_stack_height - shorter_than_second

    # L3
    taller_than_third = 10 # the fourth stack was 10 blocks taller than the third stack
    fourth_stack_height = third_stack_height + taller_than_third

    # L4
    multiplier_for_fifth = 2 # the fifth stack has twice as many blocks as the second stack
    fifth_stack_height = second_stack_height * multiplier_for_fifth

    # L5
    total_blocks = first_stack_height + second_stack_height + third_stack_height + fourth_stack_height + fifth_stack_height

    # FA
    answer = total_blocks
    return answer
def solve():
    """Index: 5672.
    Returns: the total number of toy blocks Pablo used.
    """
    # L1
    first_stack_height = 5 # The first stack was 5 blocks tall.
    taller_than_first = 2 # The second stack was 2 blocks taller than the first.
    second_stack_height = first_stack_height + taller_than_first

    # L2
    shorter_than_second = 5 # The third stack was 5 blocks shorter than the second stack
    third_stack_height = second_stack_height - shorter_than_second

    # L3
    taller_than_third = 5 # the last stack was 5 blocks taller than the third stack
    last_stack_height = third_stack_height + taller_than_third

    # L4
    total_blocks = first_stack_height + second_stack_height + third_stack_height + last_stack_height

    # FA
    answer = total_blocks
    return answer
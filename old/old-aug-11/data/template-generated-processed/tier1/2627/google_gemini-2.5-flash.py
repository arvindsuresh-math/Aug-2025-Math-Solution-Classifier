def solve():
    """Index: 2627.
    Returns: the total number of blocks used in the pyramid.
    """
    # L1
    first_row_blocks = 9 # In the first row, he has 9 blocks
    decrease_per_row = 2 # 2 less than the blocks
    second_row_blocks = first_row_blocks - decrease_per_row

    # L2
    third_row_blocks = second_row_blocks - decrease_per_row

    # L3
    fourth_row_blocks = third_row_blocks - decrease_per_row

    # L4
    fifth_row_blocks = fourth_row_blocks - decrease_per_row

    # L5
    total_blocks = first_row_blocks + second_row_blocks + third_row_blocks + fourth_row_blocks + fifth_row_blocks

    # FA
    answer = total_blocks
    return answer
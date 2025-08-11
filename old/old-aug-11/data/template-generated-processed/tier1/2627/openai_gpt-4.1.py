def solve():
    """Index: 2627.
    Returns: the total number of blocks used to build the 5-level pyramid.
    """
    # L1
    first_row_blocks = 9 # first row, he has 9 blocks
    blocks_less_per_row = 2 # for the next rows, he has 2 less than the blocks from its bottom row
    second_row_blocks = first_row_blocks - blocks_less_per_row

    # L2
    third_row_blocks = second_row_blocks - blocks_less_per_row

    # L3
    fourth_row_blocks = third_row_blocks - blocks_less_per_row

    # L4
    fifth_row_blocks = fourth_row_blocks - blocks_less_per_row

    # L5
    total_blocks = first_row_blocks + second_row_blocks + third_row_blocks + fourth_row_blocks + fifth_row_blocks

    # FA
    answer = total_blocks
    return answer
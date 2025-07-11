def solve():
    """Index: 668.
    Returns: the number of building blocks that can fit into the box.
    """
    # L1
    box_height = 8 # 8 inches in height
    box_width = 10 # 10 inches in width
    box_length = 12 # 12 inches in length
    box_volume = box_height * box_width * box_length

    # L2
    block_height = 3 # 3 inches in height
    block_width = 2 # 2 inches in width
    block_length = 4 # 4 inches in length
    block_volume = block_height * block_width * block_length

    # L3
    num_blocks = box_volume / block_volume

    # FA
    answer = num_blocks
    return answer
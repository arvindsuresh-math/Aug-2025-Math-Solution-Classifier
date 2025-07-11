def solve():
    """Index: 491.
    Returns: the number of additional blocks Jess must walk to arrive at work.
    """
    # L1
    blocks_to_store = 11 # 11 blocks to the store
    blocks_to_gallery = 6 # 6 blocks to the gallery
    blocks_to_work = 8 # 8 blocks to arrive at work
    total_blocks_needed = blocks_to_store + blocks_to_gallery + blocks_to_work

    # L2
    blocks_already_walked = 5 # already walked 5 blocks
    remaining_blocks = total_blocks_needed - blocks_already_walked

    # FA
    answer = remaining_blocks
    return answer
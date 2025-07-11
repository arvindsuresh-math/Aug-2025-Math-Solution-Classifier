def solve():
    """Index: 491.
    Returns: the number of blocks Jess must still walk to arrive at work.
    """
    # L1
    to_store = 11 # walk 11 blocks to the store
    to_gallery = 6 # 6 blocks to the gallery
    to_work = 8 # final 8 blocks to arrive at work
    total_blocks = to_store + to_gallery + to_work

    # L2
    already_walked = 5 # Jess has already walked 5 blocks
    remaining_blocks = total_blocks - already_walked

    # FA
    answer = remaining_blocks
    return answer
def solve():
    """Index: 359.
    Returns: the total number of pages Rene, Lulu, and Cherry have finished reading in 240 minutes.
    """
    # L1
    rene_pages_per_60 = 30 # Rene can finish reading 30 pages in 60 minutes
    total_minutes = 240 # have been reading for 240 minutes
    minutes_per_block = 60 # WK
    num_blocks = total_minutes // minutes_per_block
    rene_pages = rene_pages_per_60 * num_blocks

    # L2
    lulu_pages_per_60 = 27 # Lulu can read 27 pages in 60 minutes
    lulu_pages = lulu_pages_per_60 * num_blocks

    # L3
    cherry_pages_per_60 = 25 # Cherry can read 25 pages in 60 minutes
    cherry_pages = cherry_pages_per_60 * num_blocks

    # L4
    total_pages = rene_pages + lulu_pages + cherry_pages

    # FA
    answer = total_pages
    return answer
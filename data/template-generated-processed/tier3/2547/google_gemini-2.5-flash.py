def solve():
    """Index: 2547.
    Returns: the total number of sections of fishing line.
    """
    # L1
    num_reels = 3 # 3 reels
    length_per_reel = 100 # 100m fishing line
    total_length_m = num_reels * length_per_reel

    # L2
    section_length_m = 10 # 10m sections
    num_sections = total_length_m / section_length_m

    # FA
    answer = num_sections
    return answer
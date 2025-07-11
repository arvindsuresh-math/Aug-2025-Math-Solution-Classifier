def solve():
    """Index: 2305.
    Returns: the length of the shorter part of the rope.
    """
    # L1
    ratio_part1 = 2 # ratio of 2:3
    ratio_part2 = 3 # ratio of 2:3
    total_ratio_parts = ratio_part1 + ratio_part2

    # L2
    total_rope_length = 40 # A 40 meters rope
    length_per_part = total_rope_length / total_ratio_parts

    # L3
    shorter_part_ratio = 2 # ratio of 2:3
    shorter_part_length = length_per_part * shorter_part_ratio

    # FA
    answer = shorter_part_length
    return answer
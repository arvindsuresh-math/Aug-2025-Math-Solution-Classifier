def solve():
    """Index: 142.
    Returns: the percentage of germs left after using both sanitizer sprays together.
    """
    # L1
    total_percent = 100 # implied total percentage
    first_spray_kill = 50 # kills 50% of germs
    after_first = total_percent - first_spray_kill

    # L2
    second_spray_kill = 25 # kills 25% of germs
    overlap_kill = 5 # 5% of the germs they kill are the same ones
    second_unique_kill = second_spray_kill - overlap_kill

    # L3
    after_both = after_first - second_unique_kill

    # FA
    answer = after_both
    return answer
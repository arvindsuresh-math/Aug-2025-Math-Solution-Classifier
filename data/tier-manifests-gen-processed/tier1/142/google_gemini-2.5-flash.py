def solve():
    """Index: 142.
    Returns: the percentage of germs left after using both sanitizer sprays.
    """
    # L1
    total_percentage = 100 # WK
    first_spray_kill_percentage = 50 # 50% of germs
    remaining_after_first_spray = total_percentage - first_spray_kill_percentage

    # L2
    second_spray_kill_percentage = 25 # 25% of germs
    overlap_kill_percentage = 5 # 5% of the germs they kill are the same ones
    effective_second_spray_kill_percentage = second_spray_kill_percentage - overlap_kill_percentage

    # L3
    final_percentage_left = remaining_after_first_spray - effective_second_spray_kill_percentage

    # FA
    answer = final_percentage_left
    return answer
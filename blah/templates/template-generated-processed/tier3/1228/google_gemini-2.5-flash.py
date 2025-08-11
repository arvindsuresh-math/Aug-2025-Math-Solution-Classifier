def solve():
    """Index: 1228.
    Returns: the number of days it will take to make the target number of drums of paint.
    """
    # L1
    total_drums_L1 = 18 # 18 drums of paint
    days_taken_L1 = 3 # three days
    drums_per_day = total_drums_L1 / days_taken_L1

    # L2
    target_drums = 360 # 360 drums of paint
    days_to_make_target_drums = target_drums / drums_per_day

    # FA
    answer = days_to_make_target_drums
    return answer
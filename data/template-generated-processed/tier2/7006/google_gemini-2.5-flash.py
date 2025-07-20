def solve():
    """Index: 7006.
    Returns: how much floss is left over.
    """
    # L1
    num_students = 20 # 20 students in his class
    floss_per_student = 1.5 # 1.5 yards of floss
    total_floss_needed = num_students * floss_per_student

    # L3
    floss_per_packet = 35 # each packet of floss contains 35 yards
    floss_left_over = floss_per_packet - total_floss_needed

    # FA
    answer = floss_left_over
    return answer
def solve():
    """Index: 3710.
    Returns: the time (in seconds) it took the student who came first to finish the race.
    """
    # L1
    num_last_three_students = 3 # last three students
    avg_time_last_three = 35 # 35 seconds
    sum_time_last_three = num_last_three_students * avg_time_last_three

    # L2
    total_students = 4 # All 4 students
    avg_time_all_four = 30 # 30 seconds
    sum_time_all_four = total_students * avg_time_all_four

    # L3
    first_student_time = sum_time_all_four - sum_time_last_three

    # FA
    answer = first_student_time
    return answer
def solve():
    """Index: 5044.
    Returns: the number of full-day students.
    """
    # L1
    total_students = 80 # 80 students
    half_day_percent_num = 25 # 25% of them
    percent_factor = 0.01 # WK
    num_half_day_students = total_students * half_day_percent_num * percent_factor

    # L2
    num_full_day_students = total_students - num_half_day_students

    # FA
    answer = num_full_day_students
    return answer
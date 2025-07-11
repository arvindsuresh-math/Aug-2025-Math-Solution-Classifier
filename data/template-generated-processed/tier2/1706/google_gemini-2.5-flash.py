def solve():
    """Index: 1706.
    Returns: the number of students that play soccer.
    """
    # L1
    total_students = 400 # 400 students in the senior class
    sports_percentage_decimal = 0.52 # 52% of the students play sports
    students_play_sports = total_students * sports_percentage_decimal

    # L2
    soccer_percentage_decimal = 0.125 # 12.5% play soccer
    students_play_soccer = students_play_sports * soccer_percentage_decimal

    # FA
    answer = students_play_soccer
    return answer
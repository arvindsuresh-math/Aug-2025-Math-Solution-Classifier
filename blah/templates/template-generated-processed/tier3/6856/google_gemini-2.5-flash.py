def solve():
    """Index: 6856.
    Returns: the number of students who play both hockey and tennis.
    """
    # L1
    total_students = 600 # 600 students at River Falls High School
    tennis_numerator = 3 # 3/4 of them play tennis
    tennis_denominator = 4 # 3/4 of them play tennis
    students_play_tennis = tennis_numerator / tennis_denominator * total_students

    # L2
    hockey_percentage_numerator = 60 # 60% of them also play hockey
    hockey_percentage_denominator = 100 # 60% of them also play hockey
    students_play_hockey_and_tennis = hockey_percentage_numerator / hockey_percentage_denominator * students_play_tennis

    # FA
    answer = students_play_hockey_and_tennis
    return answer
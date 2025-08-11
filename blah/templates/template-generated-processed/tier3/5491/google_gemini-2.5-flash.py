def solve():
    """Index: 5491.
    Returns: the number of students going to the tournament.
    """
    # L1
    total_students = 24 # 24 students in class
    chess_program_denominator = 3 # one-third are in the after-school chess program
    students_in_program = total_students / chess_program_denominator

    # L2
    tournament_absent_denominator = 2 # half of those students
    students_going_to_tournament = students_in_program / tournament_absent_denominator

    # FA
    answer = students_going_to_tournament
    return answer